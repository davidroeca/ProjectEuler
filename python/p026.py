"""
Problem 26:

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2  =       0.5
    1/3  =       0.(3)
    1/4  =       0.25
    1/5  =       0.2
    1/6  =       0.1(6)
    1/7  =       0.(142857)
    1/8  =       0.125
    1/9  =       0.(1)
    1/10 =       0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""

def get_dividend(num, carry):
    dividend = carry * 10
    num_zeros = 0
    while num > dividend:
        num_zeros += 1
        dividend *= 10
    return dividend, num_zeros

def div_zeros_to_rep_count(prev_dividends_slice):
    return sum([num_zeros + 1 for dividend, num_zeros in prev_dividends_slice])

def get_repeat_length(carry, divisor, prev_dividends):
    if carry == 0:
        return 0
    div_zeros_tup = get_dividend(divisor, carry)
    if div_zeros_tup in prev_dividends:
        start = prev_dividends.index(div_zeros_tup)
        return div_zeros_to_rep_count(prev_dividends[start:])
    dividend, num_zeros = div_zeros_tup
    prev_dividends.append(div_zeros_tup)
    remainder = dividend % divisor
    return get_repeat_length(remainder, divisor, prev_dividends)

def denom_with_longest_recurring_cycle(rng):
    repeat_rng = {num:get_repeat_length(1, num, []) for num in rng}
    return max(repeat_rng, key=repeat_rng.get)

def main():
    rng = xrange(1, 1000)
    print denom_with_longest_recurring_cycle(rng)

if __name__ == "__main__":
    main()
