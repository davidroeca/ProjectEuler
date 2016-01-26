'''
Problem 50:

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
'''

from datetime import datetime
from p007 import prime_gen

def find_longest_cons_prime_sum(below_num):
    '''See function name

    :param below_num: INT search for consecutives below this number
    :yields: TUPLE(INT primes with sum of consecutive primes, INT n consecutive)
    '''
    primes_below_num = [i for i in prime_gen(max_val=below_num)]
    max_sum = 0
    max_len = 0
    curr_result = (max_sum, max_len)
    n_primes_below_num = len(primes_below_num)
    for i in xrange(n_primes_below_num - 1, -1, -1):
        for j in xrange(i-1, -1, -1):
            candidate = sum(primes_below_num[j:i+1])
            curr_len = i - j + 1
            if candidate > below_num:
                break
            elif candidate in primes_below_num[i+1:]:
                max_sum, max_len = curr_result
                if curr_len > max_len:
                    curr_result = (candidate, curr_len)
    return curr_result


def main():
    time_start = datetime.now()
    print find_longest_cons_prime_sum(1000000)
    time_diff = datetime.now() - time_start
    print "It took {} mins ({} seconds) to complete".format(
            time_diff.total_seconds()/60, time_diff.total_seconds())

if __name__ == "__main__":
    main()

