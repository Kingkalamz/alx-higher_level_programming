#!/usr/bin/python3
# File: 3-to_json_string.py
# Auth: Musa_kalamz A Ogunsolu

"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
