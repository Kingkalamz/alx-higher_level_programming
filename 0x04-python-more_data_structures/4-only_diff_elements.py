#!/usr/bin/python3
# File: 4-only_diff_elements.py
# Auth: Musa_kalamz A Ogunsolu


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    return (set_1 ^ set_2)
