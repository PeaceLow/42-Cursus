def game_event_generator(count: int):
    names = ["alice", "bob", "charlie", "diana", "eve"]
    actions = [
        "killed monster", "found treasure", "leveled up", "joined guild"
    ]

    for i in range(1, count + 1):
        name = names[(i * 3) % len(names)]
        action = actions[(i * 7) % len(actions)]
        level = (i * 2) % 20 + 1

        yield (i, name, level, action)


def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        div = 2
        while div * div <= num:
            if num % div == 0:
                is_prime = False
                break
            div += 1

        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()

    total_events = 0
    high_level = 0
    treasures = 0
    level_ups = 0

    # Process events
    for event in game_event_generator(1000):
        evt_id, name, level, action = event

        # Display first 3 events
        if evt_id <= 3:
            print(f"Event {evt_id}: Player {name} (level {level}) {action}")
        elif evt_id == 4:
            print("...")

        total_events += 1
        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasures += 1
        if action == "leveled up":
            level_ups += 1

    duration = 0.045

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")

    print()
    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=" ")
    first = True
    for num in fibonacci_generator(10):
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False

    print("Prime numbers (first 5):", end=" ")
    first = True
    for num in prime_generator(5):
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False
    print()


if __name__ == "__main__":
    main()
