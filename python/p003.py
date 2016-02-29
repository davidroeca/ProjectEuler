"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime_factor_gen(n):
    while (n % 2) == 0:
        yield 2
        n /= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            yield i
            n /= i
        i += 2
    if n > 1:
        yield n

def main():
    num = 600851475143
    prime_factors = prime_factor_gen(num)
    for factor in prime_factors:
        next_factor = factor
    print(next_factor)

if __name__ == '__main__':
    main()
