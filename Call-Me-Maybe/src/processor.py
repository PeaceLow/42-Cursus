import os
import json
import regex as re
from typing import Dict, List, Optional
import numpy as np
from time import time

# We import the LLM SDK dynamically to avoid crash if not installed,
# although the project requires it to be present at runtime.
from llm_sdk import Small_LLM_Model  # type: ignore

from src.models import FunctionDefinition, FunctionCallResult

GREEN = "\033[92m"
PURPLE = "\033[95m"
BOLD = "\033[1m"
CLEAR = "\033[0m"


class ConstrainedJSONDecoder:
    """Implement constrained decoding for LLM JSON generation."""

    def __init__(
        self, model: Small_LLM_Model,
        functions: List[FunctionDefinition]
    ) -> None:
        self.model = model
        self.functions = functions

        # Load vocabulary to constrain logits
        self.vocab: Dict[int, str] = {}
        try:
            vocab_path = self.model.get_path_to_tokenizer_file()
            with open(vocab_path, "r", encoding="utf-8") as f:
                tokenizer_data = json.load(f)
                vocab_dict = tokenizer_data.get("model", {}).get("vocab", {})
                # HuggingFace tokenizers have varied internals.
                # This is a best-effort fallback:
                for token_str, token_id in vocab_dict.items():
                    clean_str = token_str.replace("Ġ", " ").replace(
                        "Ċ", "\n").replace("ĉ", "\n")
                    self.vocab[token_id] = clean_str
        except Exception as e:
            print(f"Warning: Could not load vocabulary accurately. {e}")

        # We will use python regex but to avoid backtracking we make it strict
        fn_regexes = []
        for fn in self.functions:
            # strictly no spaces
            pattern = (
                r'\{"name":"'
                + fn.name
                + r'","parameters":\{'
            )

            param_patterns = []
            for p_name, p_def in fn.parameters.items():
                if p_def.type in ('number', 'float'):
                    val_pattern = r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?'
                elif p_def.type == 'integer':
                    val_pattern = r'-?(?:0|[1-9][0-9]*)'
                elif p_def.type == 'string':
                    val_pattern = r'"(?:[^"\\]|\\.)*"'
                elif p_def.type == 'boolean':
                    val_pattern = r'(?:true|false)'
                else:
                    val_pattern = r'".*?"'

                param_patterns.append(
                    r'"' + p_name + r'":' + val_pattern
                )

            pattern += r','.join(param_patterns)
            pattern += r'\}\}'
            fn_regexes.append(pattern)

        # Allow explicit fallback function call
        fn_regexes.append(r'\{"name":"no_tool_match","parameters":\{\}\}')

        # Allow empty json object if no function matches
        fn_regexes.append(r'\{\}')

        final_regex = r'^\s*(?:' + r'|'.join(fn_regexes) + r')\s*$'
        self.compiled_regex = re.compile(final_regex)

    def is_valid_json_prefix(self, prefix: str) -> bool:
        # Fast stripped
        stripped = prefix.replace(' ', '').replace('\n', '')
        if not stripped:
            return True
        return self.compiled_regex.match(stripped, partial=True) is not None

    @staticmethod
    def _to_input_id_list(encoded_ids: object) -> List[int]:
        """Convert encoded token IDs to a flat list of integers."""
        tolist_method = getattr(encoded_ids, "tolist", None)
        if callable(tolist_method):
            encoded_ids = tolist_method()

        if isinstance(encoded_ids, np.ndarray):
            encoded_ids = encoded_ids.tolist()

        if isinstance(encoded_ids, list):
            if encoded_ids and isinstance(encoded_ids[0], list):
                encoded_ids = encoded_ids[0]
            return [int(token_id) for token_id in encoded_ids]

        raise TypeError("Model encode output must"
                        "be convertible to list[int].")

    def generate(
        self, prompt: str, max_tokens: int = 150
    ) -> Optional[FunctionCallResult]:
        """Generate a constrained JSON output for the given prompt."""

        compact_funcs = []
        for fn in self.functions:
            compact_funcs.append({
                "name": fn.name,
                "description": fn.description,
                "parameters": {k: v.type for k, v in fn.parameters.items()}
            })
            
        compact_funcs.append({
            "name": "no_tool_match",
            "description": "Must be used if and only if NO other tool is suitable or matches the user's prompt.",
            "parameters": {}
        })

        funcs_schema = json.dumps(compact_funcs, separators=(',', ':'))

        sys_prompt = (
            "You are a precise API routing agent. Your job is to select the perfect function for the user's query.\n"
            f"AVAILABLE FUNCTIONS:\n{funcs_schema}\n\n"
            "CRITICAL RULES:\n"
            "1. You MUST NOT use string manipulation or regex functions (like fn_substitute_string_with_regex) for math calculations (addition, square root, etc.) or unrelated tasks.\n"
            "2. If the user's prompt asks for an action (like math, greeting, etc.) and there is NO specific function designed for that exact action, you MUST give up and use the 'no_tool_match' tool.\n"
            "3. DO NOT force a fit. If unsure, use 'no_tool_match'.\n"
            "Output ONLY the JSON object."
        )
        full_prompt = f"{sys_prompt}\nQuery: {prompt}\nJSON: {{"

        raw_input_ids = self.model.encode(full_prompt)
        input_ids = self._to_input_id_list(raw_input_ids)

        generated_text = "{"
        generated_ids: List[int] = []

        for _ in range(max_tokens):
            logits = self.model.get_logits_from_input_ids(input_ids)

            logits_arr = np.array(logits)
            if logits_arr.ndim > 1:
                logits_arr = logits_arr.flatten()

            top_k = min(400, len(logits_arr))
            top_k_indices = np.argpartition(logits_arr, -top_k)[-top_k:]
            sorted_token_ids = top_k_indices[
                np.argsort(logits_arr[top_k_indices])[::-1]
            ]

            base_text = generated_text
            proposed_text = base_text

            next_token_id = None
            for token_id in sorted_token_ids:
                token_id = int(token_id)
                # Approximate token string by decoding just the token
                # This avoids O(N^2) decoding in the inner loop
                try:
                    token_str = self.model.decode([token_id])
                except Exception:
                    continue

                proposed_text = base_text + token_str

                if self.is_valid_json_prefix(proposed_text):
                    next_token_id = token_id
                    break
                else:
                    # Attempt to escape quotes in the token and see if it becomes valid
                    if '"' in token_str:
                        escaped_token_str = token_str.replace('"', '\\"')
                        if self.is_valid_json_prefix(base_text + escaped_token_str):
                            next_token_id = token_id
                            token_str = escaped_token_str
                            proposed_text = base_text + token_str
                            break

            if next_token_id is None:
                next_token_id = int(sorted_token_ids[0])
                token_str = self.model.decode([next_token_id])
                if '"' in token_str and not self.is_valid_json_prefix(base_text + token_str):
                    token_str = token_str.replace('"', '\\"')
                proposed_text = base_text + token_str

            input_ids.append(next_token_id)
            generated_ids.append(next_token_id)

            generated_text = proposed_text

            if generated_text.strip().endswith("}"):
                try:
                    data = json.loads(generated_text)
                    if isinstance(data, dict):
                        # Proper JSON formed, we stop iterating.
                        break
                except json.JSONDecodeError:
                    pass

        try:
            # Look for the last `}` character which guarantees we have
            # captured our dictionary.
            end_index = generated_text.rfind("}")
            if end_index != -1:
                clean_json = generated_text[:end_index+1]
            else:
                clean_json = generated_text

            # We enforce Pydantic parsing
            data = json.loads(clean_json)
            
            if not data:
                return FunctionCallResult(
                    prompt=prompt,
                    error="No matching function"
                )
                
            func_name = data.get("name", "unknown")
            
            if func_name == "no_tool_match":
                return FunctionCallResult(
                    prompt=prompt,
                    error="No matching function"
                )
                
            parameters = data.get("parameters", {})

            for fn in self.functions:
                if fn.name == func_name:
                    for p_name, p_val in parameters.items():
                        if p_name in fn.parameters:
                            p_type = fn.parameters[p_name].type
                            if p_type in ('number', 'float'):
                                try:
                                    parameters[p_name] = float(p_val)
                                except (ValueError, TypeError):
                                    pass
                            elif p_type == 'integer':
                                try:
                                    parameters[p_name] = int(p_val)
                                except (ValueError, TypeError):
                                    pass
                    break

            return FunctionCallResult(
                prompt=prompt,
                name=func_name,
                parameters=parameters
            )
        except json.JSONDecodeError:
            print(f"Failed to generate valid JSON: {generated_text}")
            return None


def process_prompts(
    prompts: List[Dict[str, str]],
    functions: List[FunctionDefinition],
    output_path: str
) -> None:
    """Run the decoding pipeline on all prompts and write results."""

    try:
        model = Small_LLM_Model()
        decoder = ConstrainedJSONDecoder(model, functions)

        total_results = []
        for prompt_data in prompts:
            time_start = time()
            prompt_text = prompt_data.get("prompt", "")
            if not prompt_text:
                continue

            print(f"\n{PURPLE}{BOLD}Processing: {prompt_text}{CLEAR}")
            result = decoder.generate(prompt_text)

            if result:
                total_results.append(result.model_dump(exclude_none=True))
            else:
                # Fallback to prevent entirely missing output
                total_results.append(
                    {"prompt": prompt_text, "error": "Failed to generate valid output"})

            time_end = time()
            print(f"{GREEN}{BOLD}Processing time for this prompt: "
                  f"{time_end - time_start:.2f} seconds{CLEAR}")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        output_dir = os.path.dirname(output_path)
        if output_dir:
            try:
                os.makedirs(output_dir, exist_ok=True)
            except OSError as e:
                print(f"Could not save output, {e}")
                return

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(total_results, f, indent=4, ensure_ascii=False)
            print(
                f"Processed {len(total_results)} prompts. "
                f"Saved to {output_path}."
            )
        except OSError as e:
            print(f"Failed to write output to {output_path}: {e}")

    except Exception as e:
        print(f"Critical error during processing: {e}")
