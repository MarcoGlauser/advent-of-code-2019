from day6.puzzle1 import build_orbit_map, traverse_map


def reverse_lookup(value, orbit_map):
    for gravity_provider, orbiters in orbit_map.items():
        if value in orbiters:
            return gravity_provider


def count_if_you_or_santa(counter, candidates):
    if 'YOU' in candidates or 'SAN' in candidates:
        return counter - 1
    else:
        return 0


if __name__ == '__main__':
    orbit_map = build_orbit_map('input.txt')
    traversed = set()
    counter = 0
    total = 0
    YOU = 'YOU'
    SANTA = 'SAN'
    traversed.add(YOU)
    traversed.add(SANTA)
    stop = None
    while stop is None:
        YOU = reverse_lookup(YOU, orbit_map)
        if YOU in traversed:
            stop = YOU
            break
        else:
            traversed.add(YOU)
        SANTA = reverse_lookup(SANTA, orbit_map)
        if SANTA in traversed:
            stop = SANTA
            break
        else:
            traversed.add(SANTA)
    total = traverse_map(orbit_map, stop, count_if_you_or_santa)
    print(total)
