#!/usr/bin/python3

index = 0
for letters in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(letters - index)), end="")
    index = 32 if index == 0 else 0
