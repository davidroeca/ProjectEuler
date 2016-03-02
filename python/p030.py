"""
Problem 30:

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
def list_digits(n):
    return (int(c) for c in str(n))

def sum_digits_power(n, p):
    return sum(d ** p for d in list_digits(n))

def upper_bound_term(p):
    n = 9
    while sum_digits_power(n, p) >= n:
        n = n * 10 + 9
    return n

def get_sum_equal_power_sums(p):
    s = 0
    maximum = upper_bound_term(p)
    return sum(n for n in range(2, maximum) if n == sum_digits_power(n, p))

def main():
    print(get_sum_equal_power_sums(5))

if __name__ == "__main__":
    main()
