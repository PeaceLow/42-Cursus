from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")

        total = sum(data)
        avg = total / len(data) if data else 0
        result = (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={avg}"
        )
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        )


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")

        length = len(data)
        words = len(data.split())
        result = f"Processed text: {length} characters, {words} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")

        parts = data.split(":", 1)
        level = parts[0]
        message = parts[1].strip() if len(parts) > 1 else ""
        result = f"{level} level detected: {message}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result: str) -> str:
        prefix = "[INFO]"
        if "ERROR" in result:
            prefix = "[ALERT]"
        return f"{prefix} {super().format_output(result)}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    # Numeric Processor
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
        try:
            print(f"Output: {num_proc.process(num_data)}")
        except ValueError as e:
            print(f"Error: {e}")
    print()

    # Text Processor
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        try:
            print(f"Output: {text_proc.process(text_data)}")
        except ValueError as e:
            print(f"Error: {e}")
    print()

    # Log Processor
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        try:
            print(f"Output: {log_proc.process(log_data)}")
        except ValueError as e:
            print(f"Error: {e}")
    print()

    # Polymorphic Demo
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    tasks = [
        (num_proc, [1, 2, 3]),
        (text_proc, "Hello Python"),
        (log_proc, "INFO: System ready")
    ]

    count = 1
    for proc, data in tasks:
        try:
            result = proc.process(data)
            print(f"Result {count}: {result}")
            count += 1
        except ValueError as e:
            print(f"Skipping invalid data: {e}")

    print("Foundation systems online. Nexus ready for advanced streams.")
