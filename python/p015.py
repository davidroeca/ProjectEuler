"""
Problem 15:
Starting in the top left corner of a 2x2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.
How many such routes are there through a 20x20 grid?
"""
from functools import reduce

def factorial(n):
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

def get_num_routes(dimension):
    dim_fact = factorial(dimension)
    return factorial(2 * dimension) / (dim_fact * dim_fact)

def main():
    dimension = 20
    print(get_num_routes(dimension))

if __name__ == '__main__':
    main()
