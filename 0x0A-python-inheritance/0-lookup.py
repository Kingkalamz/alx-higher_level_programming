#!/usr/bin/python3
# Fole: 0-lookup.py
# Auth: Musa_kalamz A Ogunsolu

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
