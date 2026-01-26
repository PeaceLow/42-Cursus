#!/usr/bin/env python3

import sys


def ft_command_quest(args) -> None:
    if len(args) <= 1:
        print("No arguments provided!")

    print("Program name:", args[0])
    if len(args) > 1:
        print("Arguments received:", len(args) - 1)
        i = 1
        while i < len(args):
            print("Argument ", i, ": ", args[i], sep="")
            i += 1
    print("Total arguments:", len(args))


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest(sys.argv)
