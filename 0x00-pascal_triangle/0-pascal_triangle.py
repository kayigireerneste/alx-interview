#!/usr/bin/env python3
from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    '''
    Generate Pascal's Triangle up to n rows.
    '''
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Compute the inner elements as the sum of two elements above
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
