"""
Problem 13:

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(In problem_files/p013)
"""

import fileinput

def line_to_int(line):
    return int(line.rstrip('\n'))

def get_numbers_from_file(filename):
    f = fileinput.input(filename)
    return [line_to_int(line) for line in f]

def main():
    filename = "problem_files/p013.txt"
    # Not most optimal but works in this context
    print str(sum(get_numbers_from_file(filename)))[0:10]

if __name__ == '__main__':
    main()
