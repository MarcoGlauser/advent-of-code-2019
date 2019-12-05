import itertools

input = '240920-789857'
inputs = input.split('-')
start = int(inputs[0])
end = int(inputs[1])
initial = [int(x) for x in inputs[0]]


def predicate(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            return True
    return False


def generate_combinations(initial_numbers):
    number_of_combinations = 0
    current = initial_numbers.copy()
    current_number = int(''.join(map(str, current)))
    while current_number < end:
        if predicate(current):
            number_of_combinations += 1
        numbers_to_fold_over = []

        for i in range(5, -1, -1):
            if current[i] == 9:
                numbers_to_fold_over.append(i)
            else:
                break
        current[5-len(numbers_to_fold_over)] += 1
        for i in numbers_to_fold_over:
            current[i] = current[5-len(numbers_to_fold_over)]

        current_number = int(''.join(map(str, current)))
    return number_of_combinations


for x in range(0, 5):
    if initial[x] > initial[x+1]:
        initial[x:] = [initial[x]]*(6-x)
        break

print(generate_combinations(initial))
