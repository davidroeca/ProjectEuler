'''
Problem 42:

The nth term of the sequence of triangle numbers is given by, tn = 1/2*n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''
import os
def get_num_val(s):
    return sum(ord(i) - 64 for i in s)

def is_square(n):
    if n == 1:
        return True
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + n // x) // 2
        if x in seen:
            return False
        else:
            seen.add(x)
    return True

def is_triangle_word(w):
    val = get_num_val(w)
    n = 1 + 8 * val # from quadratic formula reversing tn
    return is_square(n)

def count_triangle_words(words):
    return sum(1 if is_triangle_word(w) else 0 for w in words)

def main():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'problem_files/p042.txt'), 'r') as f:
        text = f.read().strip().replace('"', '')
    words = text.split(',')
    print count_triangle_words(words)
    
if __name__ == "__main__":
    main()
