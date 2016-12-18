"""

Common Algorithms

@author: Naimish Agarwal
"""


import math
import fundamental_data_structures as fds
from numba import jit


@jit
def gcd(p, q):

    """
    Find Greatest Common Factor of integers p, q

    """
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


@jit
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
    The function assumes that each subexpression is enclosed in parenthesis.

    e.g. ( 1 + ( 2 * ( 3 / 7 ) ) )

    It is also assumed that at least one operator and two operands are present.

    e.g. 1 + 2 (valid)

    e.g. 2 (invalid)

    Parameters:
    -----------

    expression: arithmetic expression which can comprise the following:
        (, ), +, -, *, /, numbers

    all separated by whitespace.

    Returns:
    --------

    Value of expression after evaluation

    """

    expression = "( " + expression + " )"
    tokens = expression.split()
    operator_stack = fds.LinkedListStack()
    operand_stack = fds.LinkedListStack()

    for token in tokens:
        if token == "(":
            pass
        elif token in ["+", "-", "*", "/"]:
            operator = token
            operator_stack.push(operator)
        elif token == ")":
            operator = operator_stack.pop()
            num2 = operand_stack.pop()
            num1 = operand_stack.pop()

            print num1, operator, num2
            if operator == "+":
                operand = num1 + num2
            elif operator == "-":
                operand = num1 - num2
            elif operator == "*":
                operand = num1 * num2
            elif operator == "/":
                operand = num1 / num2
            operand_stack.push(operand)
        else:
            operand = float(token)
            operand_stack.push(operand)

    return operand_stack.pop()
