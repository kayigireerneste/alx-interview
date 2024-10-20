#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
needed to result in exactly n H characters in a file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations to get n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed or 0 if impossible.
    """
    if n < 2:
        return 0
    
    operations = 0
    divisor = 2

    # Reduce n by dividing by its factors starting from 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
