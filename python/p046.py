'''
Problem 46:

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
'''
from p007 import prime_gen
from p042 import is_square

def find_smallest_counter():
    curr_comp = 9
    while True:
        primes = [i for i in prime_gen(max_val=curr_comp + 1)]
        if curr_comp not in primes and not any(is_square((curr_comp - p)/2)
                for p in primes):
            return curr_comp
        curr_comp += 2

def main():
    print(find_smallest_counter())

if __name__ == "__main__":
    main()
