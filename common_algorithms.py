"""

Common Algorithms

@author: Naimish Agarwal
"""


def gcd(p, q):

    """
    Find Greatest Common Factor of integers p, q

    """
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)
