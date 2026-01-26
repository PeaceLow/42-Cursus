#!/usr/bin/env python3

import sys


def ft_score_analytics(args) -> None:
    if len(args) <= 1:
        print("No scores provided. Usage: ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores = []
    i = 1
    while i < len(args):
        try:
            score = float(args[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid score '{args[i]}' ignored.")
        i += 1

    if not scores:
        print("No valid scores to analyze!")
        return

    total_scores = len(scores)
    average_score = sum(scores) / total_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    print("Score processed:")
    print(f"Total players: {total_scores}")
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {highest_score:.2f}")
    print(f"Lowest score: {lowest_score:.2f}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics(sys.argv)