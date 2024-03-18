#!/usr/bin/python3
# File: 0-print_list_integer.py
# Auth: Musa_kalamz A Ogunsolu


def print_list_integer(my_list=[]):
    """Prints all integers of a list."""

    for index in range(len(my_list)):
        print("{:d}".format(my_list[index]))
