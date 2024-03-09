#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if num1 % 10 != 9 or num2 % 10 != 9:
            print("{}{}".format(num1, num2), end=", ")
        else:
            print("{}{}".format(num1, num2))
