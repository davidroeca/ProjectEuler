"""
Problem 22:

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

def names_from(filename):
    with open(filename, "r") as f:
        names_string = f.read().rstrip('\n').replace("\"", "")
        names_list = names_string.split(",")
    names_list.sort()
    return names_list

def name_val(name):
    return sum(ord(char) - 64 for char in name)

def get_score(name, num):
    return (num) * name_val(name)

def get_score_list(names):
    return [get_score(names[pos], pos + 1) for pos in range(len(names))]

def get_sum_scores(names):
    return sum(get_score_list(names))

def main():
    filename = "problem_files/p022.txt"
    names = names_from(filename)
    print(get_sum_scores(names))

if __name__ == "__main__":
    main()
