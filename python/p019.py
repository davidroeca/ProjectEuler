"""
Problem 19: 

You are given the following information, but you may prefer to do some research
for yourself.

-1 Jan 1900 was a Monday.
-Thirty days has September,
-April, June and November.
-All the rest have thirty-one,
-Saving February alone,
-Which has twenty-eight, rain or shine.
-And on leap years, twenty-nine.
-A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)
?
"""
import datetime

def get_next_sunday(d):
    return d + datetime.timedelta(6 - d.weekday())

def count_first_suns_in_date_rng(date1, date2):
    if date1 > date2:
        # reverse dates so our range works correctly
        (date1, date2) = (date2, date1)
    curr_sunday = get_next_sunday(date1)
    sunday_count = 0
    while curr_sunday < date2:
        if curr_sunday.day == 1:
            sunday_count += 1
        curr_sunday += datetime.timedelta(7)
    return sunday_count

def main():
    date1 = datetime.date(1901, 01, 01)
    date2 = datetime.date(2000, 12, 31)
    print count_first_suns_in_date_rng(date1, date2)

if __name__ == "__main__":
    main()
