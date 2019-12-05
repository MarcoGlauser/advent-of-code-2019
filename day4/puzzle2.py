from day4.puzzle1 import generate_combinations, initial


def max_two_numbers(numbers):
    padded_numbers = [-1] + numbers + [-1]
    for i in range(2, len(padded_numbers)-1):
        if padded_numbers[i] == padded_numbers[i-1] \
                and padded_numbers[i-2] != padded_numbers[i-1] \
                and padded_numbers[i+1] != padded_numbers[i]:
            return True
    return False


if __name__ == '__main__':
    print(generate_combinations(initial, max_two_numbers))