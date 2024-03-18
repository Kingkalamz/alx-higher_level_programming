#!/usr/bin/python3
# File: 8-multiple_returns.py
# Auth: Musa_kapamz A Ogunsolu


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""

    if sentence == "":
        return (0, None)

    return (len(sentence), sentence[0])
