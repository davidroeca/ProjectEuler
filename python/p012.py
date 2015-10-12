"""
Problem 12:
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be:
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def n_divisors(triangle_piece):
    n = triangle_piece
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    divisors = divisors * (count + 1)
    i = 3
    while n != 1:
        count = 0
        while n % i == 0:
            count += 1
            n = n/i
        divisors = divisors * (count + 1)
        i = i + 2
    return divisors

def piece_contribution(num):
# Triangle numbers are represented by n * (n + 1) / 2
# The factors are coprime, so there are no repeated prime factors.
# Thus, the even piece merely absorbs the extra 2 and then each can
# have separate contributions.
    if num % 2 == 0:
        return n_divisors(num / 2)
    else:
        return n_divisors(num)

def find_divisor_threshold_index(threshold):
    n = 1
    low = piece_contribution(n)
    high = piece_contribution(n + 1)
    while low * high < threshold:
        n += 1
        low = high
        high = piece_contribution(n + 1)
    return n * (n + 1) / 2

def main():
    print find_divisor_threshold_index(500)

if __name__ == '__main__':
    main()
