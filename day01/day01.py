#################################
#  Advent of Code 2019          #
#  Day 1:                       #
#  April Nickel                 #
#################################


# Get the data
with open('data.in') as f:
    data = f.read()


# Part 1
def part1(modules):
    modules = modules.splitlines()

    total_fuel = 0
    for m in modules:
        total_fuel += calculate_fuel(int(m))

    answer = total_fuel
    print('Part 1: Total fuel required: {}'.format(answer))


# Part 2
def part2(modules):
    modules = modules.splitlines()

    total_fuel = 0
    for m in modules:
        fuel = calculate_fuel(int(m))
        total_fuel += fuel
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            if fuel > 0:
                total_fuel += fuel

    answer = total_fuel
    print('Part 2: Total fuel required: {}'.format(answer))


# Helper
def calculate_fuel(mass):
    fuel = (mass // 3) - 2
    return fuel


# Do the stuff
part1(data)
part2(data)
