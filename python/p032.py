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

def sample_gen(l):
    length = len(l)
    if length == 0:
        return
    for i in l:
        removed = sample_gen([j for j in l if j != i])
        yield [i]
    for i in l:
        removed = sample_gen([j for j in l if j != i])
        for k in removed:
            yield_val = [i] + k
            if len(yield_val) < length:
                yield [i] + k

def get_multiples(l):
    for i in sample_gen(l):
        for j in sample_gen([k for k in l if k not in i]):
            yield (i, j)

def sum_pan_prods(l):
    products = set()
    lcop = list(set(l))
    lcop.sort()
    for i, j in get_multiples(lcop):
        prod = list_to_int(i) * list_to_int(j)
        digits = int_to_list(prod) + i + j
        digits.sort()
        if digits == lcop:
            products.add(prod)
    return sum(products)

def main():
    l = [i for i in xrange(1,10)]
    print sum_pan_prods(l)

if __name__ == "__main__":
    main()
