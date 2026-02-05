#!/usr/bin/env python3

import sys


def ft_score_analytics(args: list[str]) -> None:
    if len(args) <= 1:
        print("No scores provided. Usage: ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores = []
    i = 1
    while i < len(args):
        try:
            score = int(args[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid score '{args[i]}' ignored.")
        i += 1

    if not scores:
        print("No valid scores to analyze!")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    highest_score = max(scores)
    lowest_score = min(scores)

    print(f"Score processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {highest_score - lowest_score}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics(sys.argv)
