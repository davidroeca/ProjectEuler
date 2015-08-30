def is_palindrome(num):
    str_num = str(num)
    if int(str_num) == int(str_num[::-1]):
        return True
    else:
        return False

def get_biggest_pal(new_num, old_num):
    if is_palindrome(new_num) and new_num > old_num:
        return new_num
    else:
        return old_num

def main():
    biggest_pal = 0
    largest_i = 0
    largest_j = 0
    for i in xrange(1000, 100, -1):
        for j in xrange(i, 100, -1):
            biggest_pal = get_biggest_pal(i * j, biggest_pal)
    print biggest_pal

if __name__ == '__main__':
    main()
