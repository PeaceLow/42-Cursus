#!/usr/bin/env python3

def main() -> None:

    # Definition des achievements des joueurs
    alice_achievements = {
        "first_kill", "level_10", "treasure_hunter", "speed_demon"
    }
    bob_achievements = {
        "first_kill", "level_10", "boss_slayer", "collector"
    }
    charlie_achievements = {
        "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
        "perfectionist"
    }

    # Affichage des achievements
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}\n")

    # Partie analytique

    # Chaque achievement obtenu par au moins un joueur
    # (Union de tous les joueurs)
    all_achievements = alice_achievements.union(
        bob_achievements, charlie_achievements
    )

    # Commun à tous les joueurs (Intersection de tous les joueurs)
    common_all = alice_achievements.intersection(
        bob_achievements, charlie_achievements
    )

    # Achievements rares (obtenus par un seul joueur)
    # Calcul des achievements uniques à chaque joueur
    alice_unique_global = alice_achievements.difference(
        bob_achievements.union(charlie_achievements)
    )
    bob_unique_global = bob_achievements.difference(
        alice_achievements.union(charlie_achievements)
    )
    charlie_unique_global = charlie_achievements.difference(
        alice_achievements.union(bob_achievements)
    )

    rare_achievements = alice_unique_global.union(
        bob_unique_global, charlie_unique_global
    )

    # Comparaison spécifique Alice vs Bob
    alice_bob_common = alice_achievements.intersection(bob_achievements)
    alice_unique_vs_bob = alice_achievements.difference(bob_achievements)
    bob_unique_vs_alice = bob_achievements.difference(alice_achievements)

    # Affichage des analyses
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")
    print(f"Common to all players: {common_all}")
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique_vs_bob}")
    print(f"Bob unique: {bob_unique_vs_alice}")


if __name__ == "__main__":
    main()
