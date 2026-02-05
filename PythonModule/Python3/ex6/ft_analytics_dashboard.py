def main():
    players = [
        {"name": "alice", "score": 2300, "level": 15, "region": "north"},
        {"name": "bob", "score": 1800, "level": 8, "region": "east"},
        {"name": "charlie", "score": 2150, "level": 12, "region": "north"},
        {"name": "diana", "score": 2050, "level": 14, "region": "central"},
        {"name": "eve", "score": 900, "level": 4, "region": "east"},
    ]

    achievements = [
        ("alice", "first_kill"), ("alice", "level_10"),
        ("alice", "boss_slayer"), ("alice", "collector"),
        ("alice", "speed_runner"),
        ("bob", "first_kill"), ("bob", "explorer"),
        ("bob", "trader"),
        ("charlie", "level_10"), ("charlie", "boss_slayer"),
        ("charlie", "first_kill"), ("charlie", "pvp_master"),
        ("charlie", "collector"), ("charlie", "strategist"),
        ("charlie", "healer"),
        ("diana", "level_10"), ("diana", "boss_slayer"),
        ("eve", "first_kill")
    ]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    # Filter high scorers (> 2000)
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    # Scores doubled (for players with score >= 1800)
    # Using sorted to ensure consistent display order if necessary
    scores_doubled = [p["score"] * 2 for p in players if p["score"] >= 1800]
    print(f"Scores doubled: {scores_doubled}")

    # Active players (level > 5)
    active_players = [p["name"] for p in players if p["level"] > 5]
    print(f"Active players: {active_players}")
    print()

    # 3. Dict Comprehensions
    print("=== Dict Comprehension Examples ===")

    # Player scores mapping (first 3 players for demo)
    player_scores = {p["name"]: p["score"] for p in players[:3]}
    print(f"Player scores: {player_scores}")

    # Score categories
    # > 2000: high, > 1000: medium, else low
    cats = [
        "high" if p["score"] > 2000
        else "medium" if p["score"] > 1000
        else "low"
        for p in players
    ]
    # Count occurrences: map category to count
    # Use set comprehension to get unique categories for the keys
    cat_counts = {
        c: sum(1 for x in cats if x == c)
        for c in {x for x in cats}
    }
    print(f"Score categories: {cat_counts}")

    # Achievement counts per player
    # Map name to number of achievements
    unique_player_names = [p["name"] for p in players]
    ach_counts = {
        name: sum(1 for a in achievements if a[0] == name)
        for name in unique_player_names
    }

    print(f"Achievement counts: {ach_counts}")
    print()

    # 4. Set Comprehensions
    print("=== Set Comprehension Examples ===")

    # Unique players
    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    # Unique achievements
    unique_achievements = {a[1] for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    # Active regions
    active_regions = {p["region"] for p in players}
    print(f"Active regions: {active_regions}")
    print()

    # 5. Combined Analysis
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    average_score = sum(p["score"] for p in players) / len(players)
    print(f"Average score: {average_score}")

    # Top performer without using max(key=...)
    max_score = max(p["score"] for p in players)
    # Find player(s) with max score
    top_performers = [p for p in players if p["score"] == max_score]
    # Assume distinct or take first
    top_p = top_performers[0]
    top_p_ach_count = len([a for a in achievements if a[0] == top_p["name"]])

    print(
        f"Top performer: {top_p['name']} "
        f"({top_p['score']} points, {top_p_ach_count} achievements)"
    )


if __name__ == "__main__":
    main()
