#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int, float): The divisor to divide the matrix elements.

    Returns:
        list: New matrix with elements divided by the divisor rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if rows of the matrix are not of the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.

        """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
