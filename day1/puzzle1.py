from math import floor


def calculate_fuel_required(mass: int):
    return max(0, floor(mass/3) -2)


if __name__ == '__main__':
    filename = 'input.txt'
    total = 0

    with open(filename, 'r') as fp:
        for line in fp:
            total += calculate_fuel_required(int(line))

    print(total)
