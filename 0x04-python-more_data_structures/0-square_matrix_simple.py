#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        nr = []
        for n in r:
            nr.append(n ** 2)
        new_matrix.append(nr)
    return new_matrix
