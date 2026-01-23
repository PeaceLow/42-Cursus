#!/usr/bin/env python3
import subprocess
import os
import sys


def run_tests():
    """
    Runs all exercises in the Python1 project.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    exercises = [
        ("ex0", "ft_garden_intro.py"),
        ("ex1", "ft_garden_data.py"),
        ("ex2", "ft_plant_growth.py"),
        ("ex3", "ft_plant_factory.py"),
        ("ex4", "ft_garden_security.py"),
        ("ex5", "ft_plant_types.py"),
        ("ex6", "ft_garden_analytics.py"),
    ]

    print("🌱 Starting Python1 Garden Tester 🌱\n")

    for directory, filename in exercises:
        print(f"{'='*30}")
        print(f"Testing {directory}/{filename}")
        print(f"{'='*30}")

        file_path = os.path.join(base_dir, directory, filename)

        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}\n")
            continue

        try:
            # Run the command and capture output
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("✅ Execution Successful")
                print("--- Output ---")
                print(result.stdout)
                if result.stderr:
                    print("--- Stderr (Warnings) ---")
                    print(result.stderr)
            else:
                print("❌ Execution Failed")
                print("--- Error Output ---")
                print(result.stderr)
                # Print stdout anyway as it might have partial output
                if result.stdout:
                    print("--- Partial Stdout ---")
                    print(result.stdout)

        except Exception as e:
            print(f"❌ An error occurred while trying to run the script: {e}")
        print("\n")  # Add space between tests


if __name__ == "__main__":
    run_tests()
