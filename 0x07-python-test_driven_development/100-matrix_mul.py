def matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication on two matrices.

    Args:
        m_a (list): The first matrix as a list of lists.
        m_b (list): The second matrix as a list of lists.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, empty, or contains non-integer/float elements.
        ValueError: If the matrices can't be multiplied.

    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not m_a or any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not m_b or any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
