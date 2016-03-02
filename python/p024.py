"""
Problem 24:


A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
from math import factorial

def get_left_right(left_index, l):
    left_num = l[left_index]
    return ([left_num], [i for i in l if i != left_num])

def nth_permutation(n, l):
    """Assumes a sorted list l, n given less than max # permutations"""
    length = len(l)
    max_permutations = factorial(length)
    if length == 1 or n == 1:
        return l
    else:
        curr_permutation = 1
        for i in range(length):
            next_permutation = (i + 1) * factorial(length - 1)
            if n <= next_permutation:
                left, right = get_left_right(i, l)
                return left + nth_permutation(n - curr_permutation, right)
            curr_permutation = next_permutation
        raise ValueError("n is too large")

def string_nth_permutation(n, s):
    l = [i for i in s]
    l.sort()
    return "".join([str(i) for i in nth_permutation(n, l)])

def main():
    s = "0123456789"
    n = 1000000
    print(string_nth_permutation(n, s))

if __name__ == "__main__":
    main()
