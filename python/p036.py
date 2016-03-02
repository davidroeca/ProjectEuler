'''
Problem 36:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''
from p004 import is_palindrome

def max_pow_of_2(num):
    pow_of_2 = 0
    while 2 ** pow_of_2 <= num:
        pow_of_2 += 1
    return pow_of_2 - 1

def _recursive_bin_list(num, curr_pow):
    if curr_pow == -1:
        return []
    else:
        pow_of_2 = 2 ** curr_pow
        current_digit = num % pow_of_2
        digit = num // pow_of_2
        remainder = num % pow_of_2

        return  [digit] + _recursive_bin_list(remainder, curr_pow - 1) 

def to_binary_str(num):
    if num == 0:
        return "0"
    max_pow = max_pow_of_2(num)
    return "".join([str(i) for i in _recursive_bin_list(num, max_pow)])

def is_bin_palindrome(num):
    return is_palindrome(int(to_binary_str(num)))

def is_both_palindrome(num):
    return is_palindrome(num) and is_bin_palindrome(num)

def get_sum_both_palindrome(ceil):
    '''ceil is not included'''
    return sum(i for i in range(ceil) if is_both_palindrome(i))

def main():
    ceil = 1000000
    print(get_sum_both_palindrome(ceil))

if __name__ == "__main__":
    main()
