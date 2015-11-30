'''
Problem 47:

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 x 7
    15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2^2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
'''

from p005 import unique_prime_factors

def has_n_unique_factors(num, n):
    return n == len([i for i in unique_prime_factors(num)])

def get_consecutives(n_consecutive, n_distinct_factors):
    consecutives = []
    curr_int = 2
    while len(consecutives) < n_consecutive:
        if has_n_unique_factors(curr_int, n_distinct_factors):
            consecutives.append(curr_int)
        else:
            consecutives[:] = []
        curr_int += 1
    return consecutives

def find_first_consecutive(n_consecutive, n_distinct_factors):
    return get_consecutives(n_consecutive, n_distinct_factors)[0]

def main():
    print find_first_consecutive(4, 4)

if __name__ == "__main__":
    main()
