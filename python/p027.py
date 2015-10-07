"""
Problem 27:

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
-79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""
from p007 import is_prime, prime_gen
from itertools import permutations

def _evaluate_quadratic(a, b, n):
    return n * n + a * n + b

def max_consecutive_prime(a, b):
    n = 0
    while is_prime(_evaluate_quadratic(a, b, n)):
        n += 1
    return n

def a_b_gen(range_a, range_b):
    for b in range_b:
        for a in range_a:
            yield (a, b)

def get_optimal_coefficients():
    a_b_combos = a_b_gen(xrange(-999, 1000), prime_gen(max_val=1000))
    max_max_consecutive_prime, associated_prod_a_b = max(
            (max_consecutive_prime(a, b), a * b)
            for a, b in a_b_combos
            )
    return associated_prod_a_b

def main():
    print get_optimal_coefficients()
    
if __name__ == "__main__":
    main()
