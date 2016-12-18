"""

Common Algorithms

@author: Naimish Agarwal
"""


import math
import fundamental_data_structures as fds


def gcd(p, q):

    """
    Find Greatest Common Factor of integers p, q

    """
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


def is_prime(n):
    """

    Returns whether n is a prime number or not

    """

    if n < 2:
        return False

    for i in xrange(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


def evaluate_arithmetic_expression(expression):
    """

    Evaluate an arithmetic expression using Dijkstra's two stack algorithm.

    Parameters:
    -----------

    expression: arithmetic expression which can comprise the following:
        (, ), +, -, *, /, numbers

    all separated by spaces.

    Returns:
    --------

    Value of expression after evaluation

    """

    tokens = expression.split()

    for token in tokens:
        pass
