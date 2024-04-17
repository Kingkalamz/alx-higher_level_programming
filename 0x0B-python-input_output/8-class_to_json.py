#!/usr/bin/python3
# File: -class_to_json.py
# Auth: Musa_kalamz A Ogunsolu

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
