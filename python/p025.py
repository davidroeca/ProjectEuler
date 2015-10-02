"""
Problem 25:

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""
from p002 import fib_gen

def first_fib_index_n_digits(n):
    for i, v in enumerate(fib_gen(1, 1, pow(10, n + 1))):
        t1, t2 = v
        if len(str(t2)) == n:
            return i + 2 # 1-index plus 1 (since index is of t1)

def main():
    print first_fib_index_n_digits(1000)

if __name__ == "__main__":
    main()
