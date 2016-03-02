"""
Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

def last_n_digits(num, n):
    return num % pow(10, n)

def trim_power_of_10(num, power):
    return int(num / pow(10, power))

class LetterCounter(object):
    """Only works up to 4-digit numbers"""
    def __init__(self):
        num_to_letters = {
                0: "",
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen",
                20: "twenty",
                30: "thirty",
                40: "forty",
                50: "fifty",
                60: "sixty",
                70: "seventy",
                80: "eighty",
                90: "ninety",
                }
        self._100_count = len("hundred")
        self._1000_count = len("thousand")
        self._and_count = len("and")
        self._count = { key:len(val) for key, val in num_to_letters.items() }

    def count_letters(self, num):
        if num not in self._count:
            if num > 999:
                n_1000s = trim_power_of_10(num, 3)
                contrib_1000 = self._count[n_1000s] + self._1000_count
                remaining = last_n_digits(num, 3)
                self._count[num] = contrib_1000 + self.count_letters(remaining)
            elif num > 99:
                n_100s = trim_power_of_10(num, 2)
                remaining = last_n_digits(num, 2)
                if remaining:
                    and_add = self._and_count
                else:
                    and_add = 0
                contrib_100 = self._count[n_100s] + and_add + self._100_count
                self._count[num] = contrib_100 + self.count_letters(remaining)
            else:
                # 2-digit, not a teen, last digit not 0
                n_10s = trim_power_of_10(num, 1)
                contrib_10 = self._count[10 * n_10s]
                remaining = last_n_digits(num, 1)
                self._count[num] = contrib_10 + self._count[remaining]
        return self._count[num]

    def count_total_range(self, number_range):
        return sum(self.count_letters(num) for num in number_range)

def main():
     counter = LetterCounter()
     print(counter.count_total_range(range(1, 1001)))

if __name__ == "__main__":
    main()
