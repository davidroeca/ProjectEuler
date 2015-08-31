"""
Problem 6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^22 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def get_sum_range(maxnum):
    sum_range = sum((x for x in xrange(maxnum + 1)))
    return sum_range

def get_sum_difference(maxnum):
    sum_range = get_sum_range(maxnum)
    sum_diff = sum((x * (sum_range - x) for x in xrange(maxnum + 1)))
    return sum_diff

def main():
    maxnum = 100
    print get_sum_difference(maxnum)

if __name__ == '__main__':
    main()
