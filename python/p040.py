'''
Problem 40:

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
'''
def get_num_digits_per_pow(p):
    return 0 if p <= 0 else p * 9 * 10 ** (p - 1)

def digits_before_pow(p):
    lower_factors = 0 if p <= 0 else digits_before_pow(p - 1)
    return get_num_digits_per_pow(p) + lower_factors

def search_pow_of_ten(p, n):
    '''Searches range of one power of 10 to its next, for nth digit'''
    if p == 0:
        return n
    else:
        num_element = 10 ** p + n / (p + 1)
        dig_idx = (n - 1) % (p + 1) # 0-indexed
        print num_element, dig_idx
        return int(str(num_element)[dig_idx])

def get_pow_and_nth_element(digit):
    '''
    :returns: TUPLE (INT power of 10, INT # element in that power of 10)
    '''
    p = 0
    while digits_before_pow(p) < digit:
        p += 1
    return p-1, digit - digits_before_pow(p-1)

def get_nth_digit(digit):
    p, n = get_pow_and_nth_element(digit)
    print p, n
    return search_pow_of_ten(p, n)

def main():
    print reduce(lambda x, y: x * y, (get_nth_digit(10**i) for i in xrange(6)))

if __name__ == "__main__":
    main()
