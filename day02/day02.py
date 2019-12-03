#################################
#  Advent of Code 2019          #
#  Day 2: 1202 Program Alarm    #
#  April Nickel                 #
#################################


# Get the data
with open('data.in') as f:
    data = f.read()


# Part 1
def part1(int_list):
    int_list = [int(x) for x in int_list.split(",")]
    pointer = 0
    run = True
    error = False

    # replace position 1 with the value 12 and replace position 2 with the value 2
    int_list[1] = 12
    int_list[2] = 2

    while run:
        if int_list[pointer] == 1:
            int_list[int_list[pointer + 3]] = int_list[int_list[pointer + 1]] + int_list[int_list[pointer + 2]]
        elif int_list[pointer] == 2:
            int_list[int_list[pointer + 3]] = int_list[int_list[pointer + 1]] * int_list[int_list[pointer + 2]]
        elif int_list[pointer] == 99:
            run = False
        else:
            error = True
            run = False
        pointer = pointer + 4

    answer = int_list
    print('Part 1: Value: {}'.format(answer))


# Part 2
def part2(int_list):
    orig_int_list = [int(x) for x in int_list.split(",")]

    for i in range(100):
        for j in range(100):
            print('DEBUG: i, j: {}, {}'.format(i, j))
            int_list = orig_int_list[:]
            pointer = 0
            run = True
            error = False

            int_list[1] = i
            int_list[2] = j

            while run:
                if int_list[pointer] == 1:
                    int_list[int_list[pointer + 3]] = int_list[int_list[pointer + 1]] + int_list[int_list[pointer + 2]]
                elif int_list[pointer] == 2:
                    int_list[int_list[pointer + 3]] = int_list[int_list[pointer + 1]] * int_list[int_list[pointer + 2]]
                elif int_list[pointer] == 99:
                    run = False
                else:
                    error = True
                    run = False
                pointer = pointer + 4
                print('DEBUG: int_list: {}'.format(int_list))

            if int_list[0] == 19690720:
                print('Part 2: Input values: {}, {}'.format(i, j))
                print('Part 2: 100 * noun + verb = {}'.format((100 * i) + j))
                return

    print('Part 2: fini: {}'.format(int_list))


# Do the stuff
part1(data)
part2(data)