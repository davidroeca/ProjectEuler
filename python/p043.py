'''
Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
from p041 import all_pan_permutations

def get_0_9_pandigitals():
    return [i for i in all_pan_permutations(9876543210) if len(str(i)) == 10]

def has_43_property(num):
    str_num = str(num)
    divs = [2, 3, 5, 7, 11, 13, 17]
    return all(int(str_num[1+i:4+i]) % divs[i] == 0 for i in range(len(divs)))

def solve_p_43():
    return sum(i for i in get_0_9_pandigitals() if has_43_property(i))

def main():
    print(solve_p_43())

if __name__ == "__main__":
    main()
