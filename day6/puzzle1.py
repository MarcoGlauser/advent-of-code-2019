def build_orbit_map(filename):
    filename = filename
    orbit_map = {}
    with open(filename, 'r') as fp:
        for line in fp:
            orbit = line.strip().split(')')
            single_orbit = orbit_map.get(orbit[0], None)
            if single_orbit is None:
                orbit_map[orbit[0]] = {orbit[1]}
            else:
                single_orbit.add(orbit[1])
    return orbit_map


def counting_func(counter, candidates):
    return counter * len(candidates)


def traverse_map(orbit_map, head, counting_func):
    total = 0
    counter = 0
    candidates = orbit_map[head]
    while len(candidates) != 0:
        counter += 1
        total += counting_func(counter, candidates)
        previous_candidates = list(candidates)
        candidates.clear()
        for candidate in previous_candidates:
            try:
                candidates.update(orbit_map[candidate])
            except KeyError:
                pass
    return total


if __name__ == '__main__':
    orbit_map = build_orbit_map('input.txt')
    total = traverse_map(orbit_map, 'COM', counting_func)
    print(total)
