def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    
    # Simulation d'un fichier manquant pour déclencher une crise
    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt") as file:
            file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

    # Simulation d'accès à un fichier protégé pour déclencher une crise
    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt") as file:
            file.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

    # Simulation d'accès à un fichier standard pour confirmer
    # la récupération des archives
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt") as file:
            file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("SUCCESS: Archive recovered - ``Knowledge preserved for humanity''")
    print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
