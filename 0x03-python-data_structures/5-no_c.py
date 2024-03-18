#!/usr/bin/python3
# File: 5-no_c.py
# Auth: Musa_kalamz A Ogunsolu


def no_c(my_string):
    """Removes all characters c and C"""

    copy = [letter for letter in my_string if letter != 'c' and letter != 'C']
    return ("".join(copy))
