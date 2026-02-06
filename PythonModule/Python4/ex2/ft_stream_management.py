import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        q_id = "Input Stream active. Enter archivist ID: "
        arch_id = input(q_id)
        q_status = "Input Stream active. Enter status report: "
        status = input(q_status)
    except (KeyboardInterrupt, EOFError):
        return

    print()

    line1 = f"[STANDARD] Archive status from {arch_id}: {status}\n"
    sys.stdout.write(line1)

    line2 = "[ALERT] System diagnostic: Communication channels verified\n"
    sys.stderr.write(line2)

    line3 = "[STANDARD] Data transmission complete\n"
    sys.stdout.write(line3)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
