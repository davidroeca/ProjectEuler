"""
Problem 28:

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

def validate_dim(dim):
    if dim < 1:
        raise ValueError("dim must be 1 or greater")
    elif dim % 2 == 0:
        raise ValueError("dim must be odd")

def dim_to_iteration(dim):
    return dim // 2

def iteration_to_dim(iteration):
    return iteration * 2 + 1

def sum_iteration(iteration):
    if iteration == 0:
        return 1
    else:
        dim = iteration_to_dim(iteration)
        dim_below = iteration_to_dim(iteration - 1)
        dimension_piece = 4 * (dim_below) * (dim_below) 
        iteration_build = 20 * (iteration)
        return dimension_piece + iteration_build + sum_iteration(iteration - 1)

def sum_spiral_diagonal(dim):
    validate_dim(dim)
    iteration = dim_to_iteration(dim)
    return sum_iteration(iteration)

def main():
    print(sum_spiral_diagonal(1001))

if __name__ == "__main__":
    main()
