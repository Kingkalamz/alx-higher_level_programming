#!/usr/bin/python3
# File: 0-square_matrix_simple.py
# Auth: Musa_kalamz A Ohunsolu


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""

    return ([list(map(lambda num: num * num, row)) for row in matrix])
