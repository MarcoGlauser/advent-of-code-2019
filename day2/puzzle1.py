
def run_ops(ops: [int]):
    position = 0
    operation = -1
    while operation != 99:
        execute(ops, position)
        print(ops)
        position += 4
        operation = ops[position]


def execute(ops, position):
    operation = ops[position]
    a = ops[position + 1]
    b = ops[position + 2]
    result = ops[position + 3]
    if operation == 1:
        ops[result] = ops[a] + ops[b]
    if operation == 2:
        ops[result] = ops[a] * ops[b]


if __name__ == '__main__':
    filename = 'input.txt'
    ops = []
    with open(filename, 'r') as fp:
        for line in fp:
            ops = line.split(',')
            ops = list(map(int, ops))
    run_ops(ops)