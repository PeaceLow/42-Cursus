import argparse
import json
from time import time
from src.models import FunctionDefinition
from src.processor import process_prompts


def load_function_definitions(file_path: str) -> list[FunctionDefinition]:
    """Load function definitions from a JSON file."""
    try:
        with open(file_path, "r") as f:
            defs_data = json.load(f)
            return [FunctionDefinition(**d) for d in defs_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading function definitions from {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error loading function definitions: {e}")
        return []

def load_prompts(file_path: str) -> list[dict[str, str]]:
    """Load prompts from a JSON file."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            print("Error: Prompts file must contain a JSON array.")
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading prompts from {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error loading prompts: {e}")
        return []


def main() -> None:
    """Parse arguments and load function definitions and prompts."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--function_definition",
        default="data/input/functions_definition.json"
    )
    parser.add_argument(
        "--input",
        default="data/input/function_calling_tests.json"
    )
    parser.add_argument(
        "--output",
        default="data/output/function_calls.json"
    )
    args = parser.parse_args()

    functions = load_function_definitions(args.function_definition)
    prompts = load_prompts(args.input)

    num_functions = len(functions)
    num_prompts = len(prompts)
    print(f"Loaded {num_functions} function definitions and "
          f"{num_prompts} prompts.")
    time_start = time()
    process_prompts(prompts, functions, args.output)
    time_end = time()
    elapsed_time = time_end - time_start
    print(f"Total processing completed in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()
