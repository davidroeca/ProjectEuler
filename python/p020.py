from p015 import factorial

def sumdig(num):
    sumdig = 0
    remaining = num
    while remaining > 0:
        sumdig += remaining % 10
        remaining = remaining / 10
    return sumdig

def main():
    n = 100
    print sumdig(factorial(n))

if __name__ == '__main__':
    main()
