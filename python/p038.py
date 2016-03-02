'''
Problem 38:

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from functools import reduce

def get_num_str_sum(num, i):
    each_prod = (num * j for j in range(1, i + 1))
    return reduce(lambda a, b: a + b, (str(j) for j in each_prod))

def is_1_9_pandigital(n_str):
    return len(n_str) == 9 and set(n_str) == set(str(i) for i in range(1, 10))

def pan_num_gen():
    max_num = 999999 # high upper-bound
    for num in range(1, max_num):
        i = 1
        while True:
            i += 1
            current_str_sum = get_num_str_sum(num, i)
            if len(current_str_sum) > 9:
                break
            elif is_1_9_pandigital(current_str_sum):
                yield int(current_str_sum)
                break

def find_largest_pan_product_sum():
    return max(i for i in pan_num_gen())

def main():
    print(find_largest_pan_product_sum())

if __name__ == "__main__":
    main()
