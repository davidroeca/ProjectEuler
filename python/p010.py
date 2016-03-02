"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from p007 import prime_gen

def sum_primes_less_than(n):
    total_sum = 0
    primes = prime_gen()
    next_prime = next(primes)
    while next_prime < n:
        total_sum += next_prime
        next_prime = next(primes)
    return total_sum

def main():
    n = 2e6
    print(sum_primes_less_than(n))

if __name__ == '__main__':
    main()
