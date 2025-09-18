#!/usr/bin/env python3
import sys
import os
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        return

    for filename in sys.argv[1:]:
        if not os.path.exists(filename):
            if os.path.exists(filename + ".txt"):
                filename = filename + ".txt"
            else:
                print("Error")
                continue

        try:
            with open(filename, "r") as f:
                board = f.read().strip()
            if not board:
                print("Error")
                continue
            result = checkmate(board)
            print(result)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
