#!/usr/bin/python3
# File: 2-args.py
# Auth: Musa_kalamz A Ogunsolu

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for index in range(count):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
