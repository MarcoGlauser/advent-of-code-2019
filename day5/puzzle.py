import operator


def input_func():
    return int(input("Enter a number: "))


def jump_if_true(value, location):
    if value != 0:
        return location
    else:
        return None


def jump_if_false(value, location):
    if value == 0:
        return location
    else:
        return None


def finished():
    print('finished')
    exit()


opcodes = {
    '01': {
        'operation': operator.add,
        'parameters': 3,
        'output': 3,
        'modifies_position': False,
    },
    '02': {
        'operation': operator.mul,
        'parameters': 3,
        'output': 3,
        'modifies_position': False,
    },
    '03': {
        'operation': input_func,
        'parameters': 1,
        'output': 1,
        'modifies_position': False,
    },
    '04': {
        'operation': print,
        'parameters': 1,
        'output': None,
        'modifies_position': False,
    },
    '05': {
        'operation': jump_if_true,
        'parameters': 2,
        'output': None,
        'modifies_position': True,
    },
    '06': {
        'operation': jump_if_false,
        'parameters': 2,
        'output': None,
        'modifies_position': True,
    },
    '07': {
        'operation': lambda a, b: int(a < b),
        'parameters': 3,
        'output': 3,
        'modifies_position': False,
    },
    '08': {
        'operation': lambda a, b: int(a == b),
        'parameters': 3,
        'output': 3,
        'modifies_position': False,
    },
    '99': {
        'operation': exit,
        'parameters': 0,
        'output': None,
        'modifies_position': False,
    }
}


def run_ops(ops: [int], opcodes):
    position = 0
    operation = '-1'
    while int(operation) != 99:
        complete_opcode = str(ops[position]).zfill(5)
        operation = complete_opcode[3:]
        parameter_modes = complete_opcode[:3]
        position = execute(ops, position, opcodes[operation], parameter_modes)


def execute(ops, position, opcode, parameter_modes):
    number_of_input_parameters = opcode['parameters']
    input_parameters = []
    if opcode['output'] is not None:
        number_of_input_parameters -= 1

    for x in range(number_of_input_parameters):
        parameter_mode = parameter_modes[len(parameter_modes)-1-x]
        if parameter_mode == '0':
            parameter = ops[ops[position+x+1]]
        else:
            parameter = ops[position+x+1]
        input_parameters.append(parameter)

    result = opcode['operation'](*input_parameters)
    if opcode['output'] is not None:
        result_address = ops[position+opcode['output']]
        ops[result_address] = result
    if opcode['modifies_position']:
        if result is not None:
            return result
    return position + opcode['parameters'] + 1


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename, 'r') as fp:
        line = fp.readline()
        raw_ops = line.split(',')
        ops = list(map(int, raw_ops))
    run_ops(ops, opcodes)
