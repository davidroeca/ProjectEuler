from p3 import prime_factor_gen

def unique_prime_factors(num):
# generates tuples of form:
# (prime factor, # of times this factor appears)
    prime_factors = prime_factor_gen(num)
    prev_factor = 0 # initialize this value to what it cannot be
    count = 1
    for factor in prime_factors:
        if factor == prev_factor:
            count += 1
        else:
            if prev_factor != 0:
                yield (prev_factor, count)
            prev_factor = factor
            count = 1
    yield (prev_factor, count)



def smallest_num(inclusive_range):
    all_uniques = dict()
    for num in inclusive_range:
        if num == 1:
            continue
        for factor, count in unique_prime_factors(num):
            if factor not in all_uniques or all_uniques[factor] < count:
                all_uniques[factor] = count
    return reduce(
            lambda x, y: x * y,
            map(lambda k: pow(k, all_uniques[k]), all_uniques))
def main():
    inclusive_range = xrange(1, 21)
    print smallest_num(inclusive_range)
   
if __name__ == '__main__':
    main()
