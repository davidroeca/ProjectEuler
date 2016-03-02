'''
Problem 39:

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

def pythagorean_true(a, b, c):
    return a * a + b * b == c * c

def get_solns(p):
    for c in range(p // 3, p - 1):
        for b in range(1, p - c):
            a = p - c - b
            if a <= b and pythagorean_true(a, b, c):
                yield (a, b, c)

def num_solns(p):
    return len([i for i in get_solns(p)])

def p_for_max_solns(max_p=1000):
    p_solns = [(p, num_solns(p)) for p in range(1, max_p + 1)]
    return max(p_solns, key=lambda item: item[1])[0]

def main():
    print(p_for_max_solns(max_p=1000))


if __name__ == "__main__":
    main()
            
