from day2.puzzle1 import run_ops

if __name__ == '__main__':
    filename = 'input.txt'
    ops = []
    with open(filename, 'r') as fp:
        for line in fp:
            ops = line.split(',')
            ops = list(map(int, ops))
    for i in range(100):
        for j in range(100):
            ops_copy = ops.copy()
            ops_copy[1] = i
            ops_copy[2] = j
            run_ops(ops_copy)
            if ops_copy[0] == 19690720:
                print(100*i+j)
                exit()
