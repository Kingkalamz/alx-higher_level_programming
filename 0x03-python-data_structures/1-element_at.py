#!/usr/bin/python3
# File: 1-element_at.py
# Auth: Musa_kalamz A Ogunsolu


def element_at(my_list, idx):
    """Retrieves an element from a list"""

    if idx < 0 or idx > (len(my_list) - 1):
        return None

    return (my_list[idx])
