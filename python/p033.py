"""
Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

"""
from p003 import prime_factor_gen
from p032 import int_to_list, list_to_int 

def joint_frequency_dict(l1, l2):
    l1_dict = {i: l1.count(i) for i in l1}
    l2_dict = {i: l2.count(i) for i in l2}
    return {k: min(l1_dict[k], l2_dict[k])
            for k in l1_dict if k in l2_dict}

class Fraction(object):
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Cannot instantiate a fraction with denominator 0")
        self.num = num
        self.den = den

    def is_trivial(self):
        return self.num % 10 == 0 and self.den % 10 == 0

    def is_simplified(self):
        return self == self.simplified()

    def simplified(self):
        '''Produces simplified fraction
        :returns: a Fraction object with the reduced 
        '''
        if self.num == 0:
            return Fraction(0, 1)
        factors_num = [i for i in prime_factor_gen(self.num)]
        factors_den = [i for i in prime_factor_gen(self.den)]
        j_factors = joint_frequency_dict(factors_num, factors_den)
        if not j_factors:
            return Fraction(self.num, self.den)
        else:
            common_factors = [k ** v for k, v in j_factors.iteritems()]
            divide_by = reduce(lambda x, y: x * y,
                    common_factors)
            num = self.num / divide_by
            den = self.den / divide_by
            return Fraction(num, den)

    def naive_simplified(self):
        digits_num = int_to_list(self.num)
        digits_den = int_to_list(self.den)
        joint_factors = joint_frequency_dict(digits_num, digits_den)
        if not joint_factors:
            return Fraction(self.num, self.den)
        else:
            digits_num_final = [i for i in digits_num]
            digits_den_final = [i for i in digits_den]
            for k, v in joint_factors.iteritems():
                for i in xrange(v):
                    digits_num_final.remove(k)
                    digits_den_final.remove(k)
            num = list_to_int(digits_num_final)
            den = list_to_int(digits_den_final)
            if den == 0:
                # Ignore divide by zero problems
                return Fraction(0, 1)
            return Fraction(num, den).simplified()
    
    def __add__(self, other):
        a = self.simplified()
        b = other.simplified()
        gross = Fraction(a.num * b.den + b.num * a.den, a.den * b.den)
        return gross.simplified()

    def __mul__(self, other):
        a = self.simplified()
        b = other.simplified()
        gross = Fraction(a.num * b.num, a.den * b.den)
        return gross.simplified()

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return self.num != other.num or self.den != other.den

    def __str__(self):
        return "(" + str(self.num) + "/" + str(self.den) + ")"

def check_fracs_range(low, high):
    for n in xrange(low, high + 1):
        for d in xrange(n + 1, high + 1):
            fr = Fraction(n, d)
            simp = fr.simplified()
            naive = fr.naive_simplified()
            if fr != simp and simp == naive and not fr.is_trivial():
                yield simp

def main():
    print reduce(lambda x, y: x * y, check_fracs_range(10, 99)).simplified()

if __name__ == "__main__":
    main()
