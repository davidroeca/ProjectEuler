'''
Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''
from p007 import is_prime
from itertools import permutations

def flatten(it):
    return reduce(lambda x, y: x + y, it)

def all_pan_permutations(num):
    num_l = list(str(num))
    num_l.sort()
    num_str = reduce(lambda x, y: x + y, num_l)
    
    all_pandigital_strs = flatten(tuple(permutations(num_str[:i]))
        for i in xrange(1, len(num_str) + 1))
    return map(int, map(flatten, all_pandigital_strs))

def find_largest_pandigital_prime():
    max_num = 987654321
    all_pandigitals = all_pan_permutations(max_num)
    return max(i for i in all_pandigitals if is_prime(i))

def main():
    print find_largest_pandigital_prime()

if __name__ == "__main__":
    main()





