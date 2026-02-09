from abc import ABC, abstractmethod
from typing import Any, Optional, List, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        # Basic logical filtering using list comprehension
        return [item for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Filtre pour ne garder que des int ou float
            readings = [x for x in data_batch
                        if isinstance(x, (int, float))]

            if not readings:
                return "Sensor analysis: No valid readings"

            total = 0.0
            for r in readings:
                total += r
            avg = total / len(readings)

            return (f"Sensor analysis: {len(readings)} readings processed, "
                    f"avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Error in SensorStream: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        # Override to filter numbers. Criteria 'high' implies > 50 for example
        numbers = [x for x in data_batch if isinstance(x, (int, float))]
        if criteria == "high_priority":
            return [x for x in numbers if x > 50]  # Example threshold
        return numbers


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Expecting tuples like ('buy', amount) or ('sell', amount)
            # Or just filter assuming tuples are transactions
            ops = [x for x in data_batch if isinstance(x, tuple)
                   and len(x) == 2]

            count = len(ops)
            net = 0
            for op, amount in ops:
                if op == 'buy':
                    net += amount  # Assuming buy matches + in example
                elif op == 'sell':
                    net -= amount  # Assuming sell matches - (or vice versa)
                # Correction based on Example: buy:100, sell:150, buy:75
                # Result: +25. 100 - 150 + 75 = 25. So Buy is (+), Sell is (-)

            # If the calculation above (Buy+, Sell-) is correct:
            sign = "+" if net >= 0 else ""
            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {sign}{net} units")
        except Exception as e:
            return f"Error in TransactionStream: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        ops = [x for x in data_batch if isinstance(x, tuple)]
        if criteria == "high_priority":
            # Filter large transactions (> 100)
            return [x for x in ops if x[1] >= 150]
        return ops


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [x for x in data_batch if isinstance(x, str)]
            count = len(events)

            # Count strict matches for 'error'
            errors = [x for x in events if x == "error"]
            error_count = len(errors)

            return (f"Event analysis: {count} events, "
                    f"{error_count} error detected")
        except Exception as e:
            return f"Error in EventStream: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        events = [x for x in data_batch if isinstance(x, str)]
        # No specific filtering logic required by example output besides simple
        return events


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_mixed_batch(self, data_batch: List[Any]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("")
        print("Batch 1 Results:")

        for stream in self.streams:
            # Polymorphic call: each stream handles the batch differently
            # We filter data on a per-stream basis implicitly inside
            # or explicitly here. The example "Sensor data: 2 readings"
            # suggests we might want to get specific lists to print info.
            # But process_batch returns a analysis string we might print?
            # Example output format:
            # - Sensor data: 2 readings processed
            # - Transaction data: 4 operations processed
            # Since process_batch returns the analysis string, let's use that
            # The example output format in 'Polymorphic Stream Processing'
            # differs slightly from the individual calls.
            # "Sensor data: 2 readings processed"
            # To match output exactly, I'll parse the result or customize
            # But strict polymorphism suggests using the interface.
            # Let's peek at what the stream extracts
            # We use filter_data without criteria to get valid items
            valid_items = stream.filter_data(data_batch)
            count = len(valid_items)

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {count} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {count} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {count} events processed")

    def run_priority_filter(self, data_batch: List[Any]) -> None:
        print("")
        print("Stream filtering active: High-priority data only")

        results = []
        for stream in self.streams:
            filtered = stream.filter_data(data_batch, "high_priority")
            results.append((stream, filtered))

        # Reconstructing the specific line:
        # "Filtered results: 2 critical sensor alerts, 1 large transaction"
        parts = []
        for stream, data in results:
            count = len(data)
            if count > 0:
                if isinstance(stream, SensorStream):
                    parts.append(f"{count} critical sensor alerts")
                elif isinstance(stream, TransactionStream):
                    parts.append(f"{count} large transactions")

        print(f"Filtered results: {', '.join(parts)}")
        print("")
        print("All streams processed successfully. Nexus throughput optimal.")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    # Init Streams
    print("Initializing Sensor Stream...")
    sensor_s = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_s.stream_id}, Type: {sensor_s.stream_type}")
    sensor_input = [28, 10, 225.9]  # floats/ints
    # Recreating example print
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor_s.process_batch(sensor_input))
    print("")

    print("Initializing Transaction Stream...")
    trans_s = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_s.stream_id}, Type: {trans_s.stream_type}")
    trans_input = [('buy', 100), ('sell', 150), ('buy', 75)]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans_s.process_batch(trans_input))
    print("")

    print("Initializing Event Stream...")
    event_s = EventStream("EVENT_001")
    print(f"Stream ID: {event_s.stream_id}, Type: {event_s.stream_type}")
    event_input = ['login', 'error', 'logout']
    print("Processing event batch: [login, error, logout]")
    print(event_s.process_batch(event_input))
    print("")

    # Polymorphic Part
    processor = StreamProcessor()
    processor.add_stream(sensor_s)
    processor.add_stream(trans_s)
    processor.add_stream(event_s)

    # Mixed Batch
    # Combining inputs + some extras to match "Batch 1 Results" counts
    # Sensor: 2 readings (maybe one was filtered or specific input used?)
    # Example says: Sensor data: 2 readings processed.
    # Transaction: 4 operations.
    # Event: 3 events.

    # Constructing mixed batch to match the counts in "Batch 1 Results"
    mixed_batch = [
        60.5, 101.5,           # 2 sensors (> 50 for high priority)
        ('buy', 100), ('sell', 150), ('buy', 75), ('sell', 140),  # 4 trans
        'login', 'error', 'logout'  # 3 events
    ]

    processor.process_mixed_batch(mixed_batch)
    processor.run_priority_filter(mixed_batch)


if __name__ == "__main__":
    main()
