import copy

def line_to_int_list(line):
    return [int(elem) for elem in line.rstrip('\n').split(' ')]

def file_to_triangle(file_path):
    with open(file_path, "r") as f:
        lines = f.read().split("\n")
    return [line_to_int_list(line) for line in lines if line]

def max_sum_for_row(max_sum_row_below, current_row):
    """Takes 2 list references and generates new max sum list in a
    dynamic programming algorithm (references solution to prev row)"""
    row_length = len(current_row)
    return [max(max_sum_row_below[i], max_sum_row_below[i + 1]) + current_row[i]
            for i in range(row_length)]

def retrieve_max_sum_triangle(triangle):
    depth = len(triangle)
    max_sum_triangle = [copy.copy(triangle[depth - 1])]
    for i in range(1, depth):
        row = depth - i - 1
        max_sum_triangle.insert(
                0, 
                max_sum_for_row(max_sum_triangle[0], triangle[row])
                )
    return max_sum_triangle

def main(file_path="problem_files/p018.txt"):
    triangle = file_to_triangle(file_path)
    max_sum_triangle = retrieve_max_sum_triangle(triangle)
    print(max_sum_triangle[0][0])

if __name__ == "__main__":
    main()
