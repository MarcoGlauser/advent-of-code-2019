import itertools

from day5.puzzle import opcodes, run_ops

state = {
    'value': 0,
    'input': 0,
    'phase': 0,
    'best_result': (0, 0),
    'interrupt': False
}
phase_settings = list(itertools.permutations(range(5)))


def reset_state():
    state['value'] = 0
    state['input'] = 0
    state['phase'] = 0


def output_func(value):
    state['value'] = value


def input_func():
    if state['input'] == 0:
        state['input'] = 1
        return state['phase']
    else:
        state['input'] = 0
        return state['value']


opcodes['03']['operation'] = input_func
opcodes['04']['operation'] = output_func

opcodes['99'] = {
    'operation': lambda: None,
    'parameters': 0,
    'output': None,
    'modifies_position': False,
}


def loop_phases(ops):
    for index, phase_setting in enumerate(phase_settings):
        reset_state()
        for phase in phase_setting:
            state['phase'] = phase
            run_ops(ops.copy(), opcodes)
        if state['value'] > state['best_result'][1]:
            state['best_result'] = (index, state['value'])
    print(phase_settings[state['best_result'][0]])
    print(state['best_result'][1])


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename, 'r') as fp:
        line = fp.readline()
        raw_ops = line.split(',')
        ops = list(map(int, raw_ops))
    loop_phases(ops)
