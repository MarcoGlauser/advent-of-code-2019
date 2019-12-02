from math import floor

filename = 'input.txt'
total = 0


def calculate_fuel_required(mass: int):
    return floor(mass/3) -2


with open(filename, 'r') as fp:
    for line in fp:
        total += calculate_fuel_required(int(line))

print(total)
