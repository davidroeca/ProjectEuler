'''
Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial
from p032 import int_to_list, list_to_int

FACTORIAL_DICT = {i:factorial(i) for i in range(10)}

def sum_facs_eq_num(num):
    return num == sum((FACTORIAL_DICT[i] for i in int_to_list(num)))

def solve34():
    upper_bound = 2540160
    return sum((i for i in range(3, upper_bound) if sum_facs_eq_num(i)))

def main():
    print(solve34())

if __name__  == '__main__':
    main()
