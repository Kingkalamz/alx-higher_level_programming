#!/usr/bin/python3
# File: 3-infinite_add.py
# Auth: Musa_kalamz A Ogunsolu

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0

    for index in range(len(sys.argv) - 1):
        total += int(sys.argv[index + 1])
    print("{}".format(total))
