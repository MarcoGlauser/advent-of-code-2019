import itertools

from day5.puzzle import execute
from day7.puzzle1 import state, opcodes

phase_settings = list(itertools.permutations(range(5, 10)))


def input_func():
    if state['input'] % 2 == 0 and state['input'] < 10:
        state['input'] += 1
        return state['phase']
    else:
        state['input'] += 1
        return state['value']


def output_func(value):
    state['value'] = value
    state['interrupt'] = True


opcodes['03']['operation'] = input_func
opcodes['04']['operation'] = output_func


def reset_state():
    state['value'] = 0
    state['input'] = 0
    state['phase'] = 0
    state['interrupt'] = False


def run_ops(ops: [int], opcodes, position: 0):
    operation = '-1'
    while int(operation) != 99 and not state['interrupt']:
        complete_opcode = str(ops[position]).zfill(5)
        operation = complete_opcode[3:]
        parameter_modes = complete_opcode[:3]
        position = execute(ops, position, opcodes[operation], parameter_modes)
    return int(operation), position


def loop_phases(ops):
    for i, phase_setting in enumerate(phase_settings):
        reset_state()
        phase_ops = [ops.copy() for x in phase_setting]
        phase_position = [0] * len(phase_setting)
        while True:
            last_code = 0
            for j, phase in enumerate(phase_setting):
                state['phase'] = phase
                last_code, phase_position[j] = run_ops(phase_ops[j], opcodes, phase_position[j])
                if last_code != 99:
                    state['interrupt'] = False
            if last_code == 99:
                break

        if state['value'] > state['best_result'][1]:
            state['best_result'] = (i, state['value'])
    print(phase_settings[state['best_result'][0]])
    print(state['best_result'][1])


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename, 'r') as fp:
        line = fp.readline()
        raw_ops = line.split(',')
        ops = list(map(int, raw_ops))
    loop_phases(ops)