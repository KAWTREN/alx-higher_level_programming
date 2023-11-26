#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
multiplies 2 mtrices
Args:
    m_a: list of lists
    m_b: list of lists
Raise:
    TypeError: if m_b or m_a is not a list
    TypeError: if m_a or m_b is not a list of lists
    ValueError: if m_a or m_b is empty list
    TypeError: if m_a or m_b is not a list of integer or float
    TypeError: if m_a or m_b is not a rectangle
    TypeError: if m_a and m_b can't be multiplied
    Return:
        matrix : list of lists
"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must b a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not isinstance(num, (int, float))for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    #for m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must b a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(num, (int, float))for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    R = [[sum(a * b for a,b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return R