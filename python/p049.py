'''
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''
from itertools import permutations, combinations
from functools import reduce
from p007 import prime_gen

def numeric_permutations(num):
    return [int(reduce(lambda x, y: x + y, i))
            for i in permutations(str(num))]

def find_arithmetic_subset(l, sub_length):
    length = len(l)
    if length < sub_length:
        return []
    l_copy = [i for i in l]
    l_copy.sort()
    all_combs = [list(i) for i in combinations(l_copy, sub_length)]
    for c in all_combs:
        if all(c[i + 1] - c[i] == c[1] - c[0] for i in range(sub_length - 1)):
            return c
    return []

def all_4_digit_primes():
    return [i for i in prime_gen(max_val=10000) if i>= 1000]

def find_all_candidates(subset_length=3):
    primes_remaining = all_4_digit_primes()
    candidates = []
    while primes_remaining:
        current_prime = primes_remaining.pop(0)
        prime_perms = list(set([i for i in numeric_permutations(current_prime)
                if i in primes_remaining and i >= 1000]))
        for i in prime_perms:
            primes_remaining.remove(i)
        prime_perms.insert(0, current_prime)
        subset_try = find_arithmetic_subset(prime_perms, subset_length)
        candidates.append(subset_try)
    return [(l, reduce(lambda x, y: x+y, [str(i) for i in l]))
            for l in candidates if l]

def main():
    print(find_all_candidates(subset_length=3)) 

if __name__ == "__main__":
    main()
