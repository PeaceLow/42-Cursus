*This project has been created as part of the 42 curriculum by avauclai.*

## Description
**Call Me Maybe** is a project exploring the concept of function calling within Large Language Models (LLMs). The main goal is to implement and experiment with constrained decoding techniques, ensuring that an LLM outputs valid JSON objects or follows exact schemas that correspond to predefined function signatures. It aims to bridge the gap between unstructured LLM outputs and deterministic, programmatic tool use.

## Instructions
This project utilizes `uv` for dependency management and Python 3.13+.

### Installation
To set up the project and install all required dependencies (such as `pydantic`, `numpy`, and `regex`), run:
```bash
make install
```

### Execution
To run the main module, simply use:
```bash
make run
```
You can also run in debug mode using Python's `pdb`:
```bash
make debug
```

### Clean up
To remove cache directories (`__pycache__`, `.mypy_cache`, etc.):
```bash
make clean
```
To do a full clean including the virtual environment:
```bash
make fclean
```

## Resources
During the development of this project, various resources and AI tools were consulted:
- **Documentation:** Python's [pydantic](https://docs.pydantic.dev/) and `regex` documentation.
- **Articles:** Papers and blog posts on constrained decoding and grammar-based text generation in LLMs.
- **AI Usage:** Generative AI models (such as ChatGPT, GitHub Copilot) were used to assist with brainstorming test edge cases, formulating regex syntax for string parsing, parsing error debugging, and structuring some boilerplate code. Code generation was carefully reviewed to ensure comprehension and alignment with project constraints.

## Algorithm explanation
The core of this project relies on **constrained decoding** to force the LLM into generating syntactically valid function calls. The algorithm intercepts the token generation process at inference time. Using a finite state machine (FSM) or regular expression constraints built from the provided function definitions (e.g., via Pydantic schemas), the algorithm masks out any logits/tokens that would lead to an invalid JSON structure or incorrect argument types. This guarantees that the final string parsed from the LLM is well-formed and perfectly matches the expected function arguments.

## Design decisions
- **Regex-based Parsing & Constraints:** The `regex` library is heavily utilized to validate intermediate tokens against expected JSON constructs.
- **Pydantic Validation:** Used to define the schemas for the available functions, giving a robust, programmatic way to map and validate the expected JSON fields constraint against the LLM output.
- **Workspace Structure:** A modular approach using `uv workspaces` allows separating the core `llm_sdk` logic from the `moulinette` testing framework and the main `src` pipeline.

## Performance analysis
- **Accuracy:** Constrained decoding eliminates JSON syntax errors entirely (0% malformed JSON rate compared to standard unconstrained decoding), drastically improving reliability for function calling.
- **Speed:** There is a slight overhead per token due to the regex/schema matching state machine evaluating the valid token prefix. However, overall speed remains largely bound by the LLM inference itself, keeping it suitable for real-time applications.
- **Reliability:** By strictly limiting the token output space, hallucinated function parameters or missing mandatory fields are effectively eliminated.

## Challenges faced
- **State Space Complexity:** Mapping vast JSON schemas into continuous constraints required careful handling of string parsing and token boundaries.
- **Sub-word Tokenization:** Handling partial JSON strings (like generating half of a keyword) required ensuring the constraint verifier understands partial token overlaps without incorrectly rejecting valid paths.
- **Integration:** Ensuring the constraint logic perfectly syncs with the LLM's generation loop without massive performance degradation.

## Testing strategy
Validation is handled programmatically via our custom `moulinette` tool and standard unit tests. 
- Input mock definitions and definitions are parsed from `data/input/`.
- Tests run against varied edge cases (e.g., nested structures, special characters in string parameters).
```bash
make lint-strict
```

## Example usage
If provided an environment or prompt with a function `get_weather(city: str)`, the framework acts as follows:

```python
# Assuming predefined setup
from src.processor import process_prompt

response = process_prompt("What is the weather in Paris?")
# The constrained decoder forces the model to output:
# {"name": "get_weather", "arguments": {"city": "Paris"}}
print(response)
```
*(The above code is an illustration based on the structure of `src/processor.py`)*