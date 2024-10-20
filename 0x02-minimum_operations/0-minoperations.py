#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
"""


def minOperations(n: int) -> int:
    """ number of operations needed to result in exactly n H characters """
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
