#!/usr/bin/python3
# File: 9-multiply_by_2.py
# Auth: Musa_kalamz A Ogunsolu


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""

    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
