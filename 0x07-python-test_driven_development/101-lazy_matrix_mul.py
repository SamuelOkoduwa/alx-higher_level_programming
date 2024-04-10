#!/usr/bin/python3
"""Module to multiply matrices using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using NumPy

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        numpy.ndarray: Resultant matrix
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a and m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)
    result = np.dot(np_m_a, np_m_b)
    return result.tolist()