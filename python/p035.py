'''
Problem 35:

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
'''
from p007 import is_prime
from p032 import list_to_int, int_to_list

def rotations(l):
    e = len(l)
    for i in xrange(e):
        yield  l[i:e] + l[0:i]

def is_circular(n):
    l = int_to_list(n)
    return all(is_prime(list_to_int(r)) for r in rotations(l))

def n_circular_primes_below(num):
    return sum(1 for n in xrange(num) if is_circular(n))

def main():
    print n_circular_primes_below(1000000)
   

if __name__ == "__main__":
    main()
