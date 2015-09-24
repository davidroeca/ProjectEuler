"""
Problem 21:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

def sum_proper_divisors(num):
    sum_div = 1 # 1 is always a divisor
    max_check = int(sqrt(num))
    for i in xrange(2, max_check + 1):
        if num % i == 0:
            sum_div += i
            sum_div += num / i
    if max_check * max_check == num:
        sum_div -= max_check # sqrt is repeated in algorithm
    return sum_div

def amicable_nums_below(n):
    amicable_nums = []
    for a in xrange(2, n):
        if a in amicable_nums:
            continue
        b = sum_proper_divisors(a)
        if b != a and sum_proper_divisors(b) == a:
            amicable_nums.append(a)
            amicable_nums.append(b)
    return list(set(amicable_nums))

def main():
    print sum(amicable_nums_below(10000))

if __name__ == "__main__":
    main()





