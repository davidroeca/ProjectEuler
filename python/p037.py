'''
Problem 37:

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
from p007 import prime_gen

def is_trunctable(num, primes):
    strnum = str(num)
    for i in xrange(1, len(strnum)):
        if int(strnum[:-1 * i]) not in primes or int(strnum[i:]) not in primes:
            return False
    return True

def main():
    max_num = 1000000
    primes = set(i for i in prime_gen(max_num))
    print sum(i for i in primes if is_trunctable(i, primes) and i > 7)

if __name__ == "__main__":
    main()
