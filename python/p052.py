'''
Problem 51:

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''
from collections import defaultdict

def digit_mapping(n):
    d = defaultdict(int)
    for l in str(n):
        d[int(l)] += 1
    return d

def prods_have_same_digits(n, max_check):
    d = digit_mapping(n)
    return all(d == digit_mapping(n * i) for i in range(2, max_check + 1))

def main():
    i = 1
    while not prods_have_same_digits(i, 6):
        i += 1
    print(i)

if __name__ == "__main__":
    main()

