from day1.puzzle1 import calculate_fuel_required

if __name__ == '__main__':
    filename = 'input.txt'
    total = 0
    with open(filename, 'r') as fp:
        for line in fp:
            subtotal = calculate_fuel_required(int(line))
            while subtotal > 0:
                total += subtotal
                subtotal = calculate_fuel_required(subtotal)
    print(total)


