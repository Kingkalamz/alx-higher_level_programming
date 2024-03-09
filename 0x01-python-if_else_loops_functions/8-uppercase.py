#!/usr/bin/python3


def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}" .format(letter), end="")
    print("")
