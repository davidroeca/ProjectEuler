"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from functools import reduce
import sys

def is_triple(a, b, c):
    if ((a*a + b*b - c*c) == 0):
        return True
    return False

def check_possibilities(sum_a_b, c):
    for i in range(1,int(sum_a_b/2) + sum_a_b % 2):
        a = i
        b = sum_a_b - i
        if (a * a + b * b - c * c == 0):
            return [a, b, c]
    return []

def triple_given_sum(given_sum):
    '''
    Make c the biggest number, in the range of [~1/3*given_sum, given_sum - 2]
    Function assumes that there is only one triplet.
    '''
    max_sum_a_b = given_sum - (int(given_sum / 3) + given_sum % 3)
    for sum_a_b in range(2, max_sum_a_b):
        c = given_sum - sum_a_b
        check = check_possibilities(sum_a_b, c)
        if check:
            return check
    raise(ValueError("No triple given sum."))

def triple_product_given_sum(given_sum):
    triples = triple_given_sum(given_sum)
    return reduce(lambda x, y: x * y, triples)

def main():
    given_sum = 1000
    print(triple_product_given_sum(given_sum))

if __name__ == '__main__':
    main()
