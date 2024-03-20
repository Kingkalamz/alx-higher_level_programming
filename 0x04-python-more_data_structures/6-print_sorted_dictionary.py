#!/usr/bin/python3
# File: 6-print_sorted_dictionary.py
# Auth: Musa_kalamz A Ogunsolu


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
