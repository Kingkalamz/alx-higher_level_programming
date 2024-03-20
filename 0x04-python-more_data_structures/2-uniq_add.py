#!/usr/bin/python3
# File: 2-uniq_add.py
# Auth: Musa_kalamz A Ogunsolu


def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""

    result = 0
    for num in set(my_list):
        result += num
    return (result)
