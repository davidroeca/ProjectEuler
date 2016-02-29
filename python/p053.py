'''
Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = n!/(r!(n−r)!)

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater
than one-million?
'''

from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def count_choose_condition(n_max, condition):
    '''Computes a count of nCr values up to n_max based on condition function

    :param n_max: INT max n value for nCr in range starting at 1
    :param condition: FUNCTION(n) that is the basis for a conditional sum
    :returns: INT sum of all nCr values that evaluate to True for condition
    '''
    return sum(1 if condition(choose(n, r)) else 0
            for n in range(1, n_max + 1)
            for r in range(1, n + 1)
            )

if __name__ == "__main__":
    print(count_choose_condition(100, lambda n: n > 1000000))
