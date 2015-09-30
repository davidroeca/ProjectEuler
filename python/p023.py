"""
Problem 23:

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
from p021 import sum_proper_divisors

def is_abundant(number):
    return number < sum_proper_divisors(number)

def get_abundants():
    max_check = 28123
    return [num for num in xrange(1, max_check + 1) if is_abundant(num)]

def try2():
    abundants = get_abundants()
    non_abundant_sums = set(xrange(1, 28124))
    for index1, abundant_1 in enumerate(abundants):
        for abundant_2 in abundants[index1 + 1:]:
            non_abundant_sums.discard(abundant_1 + abundant_2)
    print non_abundant_sums
    return sum(non_abundant_sums)

def main():
    print try2()

if __name__ == "__main__":
    main()
