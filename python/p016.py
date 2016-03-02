"""
Problem 16:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_dig(num):
    digit_sum = 0
    while (num):
        digit_sum += num % 10
        num = int(num / 10)
    return digit_sum

def main():
    two2thousandth = 1 << 1000
    print(sum_dig(two2thousandth))

if __name__ == '__main__':
    main()
