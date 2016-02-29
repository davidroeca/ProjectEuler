"""
Problem 2:
Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not 
exceed four million, find the sum of the even-valued terms.
"""

def get_even_sum(maxterm):
    s = sum(term2 for term1, term2 in fib_gen(1, 2, maxterm) if term2 % 2 == 0)
    return s
    
def fib_gen(term1, term2, maxterm):
    yield (term1, term2)
    while term2 < maxterm:
        yield (term2, term2 + term1)
        term1, term2 = term2, term1 + term2 # simple swap operation

def main():
    maxterm = 4e6
    print(get_even_sum(maxterm))

if __name__ == '__main__':
    main()
