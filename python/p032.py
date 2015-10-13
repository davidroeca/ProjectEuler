"""
Problem 32:

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from p029 import unique_list

def list_to_int(l):
    length = len(l)
    return sum(l[i] * 10 ** (length - 1 - i) for i in xrange(length))

def int_to_list(n):
    return [int(d) for d in str(n)]

def are_prod_and_input_pandigital(a, b, pandigitals):
    pandigitals.sort()
    prod = a * b
    full_list = int_to_list(a) + int_to_list(b) + int_to_list(prod)
    full_list.sort()
    
def n_digits_gen(max_total=8):
    for total in xrange(2, max_total + 1):
        for i in xrange(1, total):
            yield (i, total - i)

def main():
    pandigital_list = int_to_list(12345789)
    print [tup for tup in n_digits_gen()]

if __name__ == "__main__":
    main()
