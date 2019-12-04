#################################
#  Advent of Code 2019          #
#  Day 4: Secure Container      #
#  April Nickel                 #
#################################


# Imports
from collections import Counter


# Get the data
with open('data.in') as f:
    data = f.read()


# Part 1
def part1(int_range):
    low, high = int_range.split("-")
    meets_criteria = 0

    # criteria: within range
    for i in range(int(low), int(high)+1):
        i_s = str(i)

        # criteria: two same adjacent digits
        if not (i_s[0] == i_s[1] or i_s[1] == i_s[2] or i_s[2] == i_s[3] or i_s[3] == i_s[4] or i_s[4] == i_s[5]):
            continue

        # criteria: digits never decrease
        if not (i_s[0] <= i_s[1] and i_s[1] <= i_s[2] and i_s[2] <= i_s[3] and i_s[3] <= i_s[4] and i_s[4] <= i_s[5]):
            continue

        # meets all criteria
        meets_criteria = meets_criteria + 1

    answer = meets_criteria
    print('Part 1: Value: {}'.format(answer))


# Part 2
def part2(int_range):
    low, high = int_range.split("-")
    meets_criteria = 0

    # criteria: within range
    for i in range(int(low), int(high)+1):
        i_s = str(i)

        # criteria: two same adjacent digits
        if not (i_s[0] == i_s[1] or i_s[1] == i_s[2] or i_s[2] == i_s[3] or i_s[3] == i_s[4] or i_s[4] == i_s[5]):
            continue

        # criteria: digits never decrease
        if not (i_s[0] <= i_s[1] and i_s[1] <= i_s[2] and i_s[2] <= i_s[3] and i_s[3] <= i_s[4] and i_s[4] <= i_s[5]):
            continue

        # additional criteria: two same adjacent digits cannot be part of larger group of matching digits
        count_dict = Counter(str(i))
        if 2 not in count_dict.values():
            continue

        print('DEBUG: {}'.format(i))
        # meets all criteria
        meets_criteria = meets_criteria + 1

    answer = meets_criteria
    print('Part 1: Value: {}'.format(answer))


# Helper
def get_digit(number, n):
    return number // 10**n % 10

# Do the stuff
part1(data)
part2(data)