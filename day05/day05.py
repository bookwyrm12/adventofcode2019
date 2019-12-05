#############################################
#  Advent of Code 2019                      #
#  Day 5: Sunny with a Chance of Asteroids  #
#  April Nickel                             #
#############################################


# Get the data
with open('data.in') as f:
    data = f.read()


# Part 1
def part1(int_list):
    int_list_orig = [int(x) for x in int_list.split(",")]
    int_list_copy = int_list_orig[:]

    output = follow_instructions(int_list_copy, 1)

    print('Part 1: {}'.format(output))


# Part 2
def part2(int_list):
    int_list_orig = [int(x) for x in int_list.split(",")]
    int_list_copy = int_list_orig[:]

    output = follow_instructions(int_list_copy, 5)

    print('Part 2: {}'.format(output))


# Helper
def follow_instructions(int_list, ac_id_input):
    pointer = 0
    run = True
    error = False
    output = []

    while run:
        instruction = str(int_list[pointer]).zfill(5)
        opcode = int(instruction[-2:])
        modes = [int(x) for x in instruction[-3::-1]]

        if opcode == 1:
            int_list[int_list[pointer + 3]] = get_param(int_list, modes, pointer, 0) + get_param(int_list, modes, pointer, 1)
            pointer = pointer + 4
        elif opcode == 2:
            int_list[int_list[pointer + 3]] = get_param(int_list, modes, pointer, 0) * get_param(int_list, modes, pointer, 1)
            pointer = pointer + 4
        elif opcode == 3:
            int_list[int_list[pointer + 1]] = ac_id_input
            pointer = pointer + 2
        elif opcode == 4:
            output.append(get_param(int_list, modes, pointer, 0))
            pointer = pointer + 2
        elif opcode == 5:
            if get_param(int_list, modes, pointer, 0) is not 0:
                pointer = get_param(int_list, modes, pointer, 1)
            else:
                output.append(0)
                pointer = pointer + 3
        elif opcode == 6:
            if get_param(int_list, modes, pointer, 0) is 0:
                pointer = get_param(int_list, modes, pointer, 1)
            else:
                output.append(0)
                pointer = pointer + 3
        elif opcode == 7:
            if get_param(int_list, modes, pointer, 0) < get_param(int_list, modes, pointer, 1):
                int_list[int_list[pointer + 3]] = 1
            else:
                int_list[int_list[pointer + 3]] = 0
            pointer = pointer + 4
        elif opcode == 8:
            if get_param(int_list, modes, pointer, 0) == get_param(int_list, modes, pointer, 1):
                int_list[int_list[pointer + 3]] = 1
            else:
                int_list[int_list[pointer + 3]] = 0
            pointer = pointer + 4
        elif opcode == 99:
            run = False
        else:
            error = True
            run = False

    return output


def get_param(int_list, modes, pointer, param_index):
    if modes[param_index] == 1:
        return int_list[pointer + param_index + 1]
    else:
        return int_list[int_list[pointer + param_index + 1]]

# Do the stuff
part1(data)
part2(data)