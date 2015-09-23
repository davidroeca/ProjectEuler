from math import sqrt

def sum_proper_divisors(num):
    sum_div = 1 # 1 is always a divisor
    max_check = int(sqrt(num))
    for i in xrange(2, max_check + 1):
        if num % i == 0:
            sum_div += i
            sum_div += num / i
    if max_check * max_check == num:
        sum_div -= max_check # sqrt is repeated in algorithm
    return sum_div

def amicable_nums_below(n):
    amicable_nums = []
    for a in xrange(2, n):
        if a in amicable_nums:
            continue
        b = sum_proper_divisors(a)
        if b != a and sum_proper_divisors(b) == a:
            amicable_nums.append(a)
            amicable_nums.append(b)
    return list(set(amicable_nums))

def main():
    print sum(amicable_nums_below(10000))

if __name__ == "__main__":
    main()





