"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    check = 3
    while check * check <= num:
        if num % check == 0:
            return False
        check += 2
    return True

def prime_gen(max_val = None):
    yield 2
    guess = 3
    while True:
        prime_not_found = True
        while prime_not_found:
            if max_val and guess > max_val:
                return
            if is_prime(guess):
                yield guess
                prime_not_found = False
            guess += 2

def nth_prime(n):
    primes = prime_gen()
    for i in range(n-1):
        next(primes)
    return next(primes)

def main():
    n = 10001
    print(nth_prime(n))
    
if __name__ == '__main__':
    main()
