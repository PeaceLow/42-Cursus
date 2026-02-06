def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print("Connection established. Retrieving data...\n")
            content = file.read()
            print("RECOVERED DATA:")
            print(content)
            file.close()
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("Error: Storage vault not found. Unable to recover data.")


if __name__ == "__main__":
    main()
