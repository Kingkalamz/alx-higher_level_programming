#!/usr/bin/python3
# File: 101-locked_class.py
# Auth: Musa_kalamz A Ogunsolu

"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
