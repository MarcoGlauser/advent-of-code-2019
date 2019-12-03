def generate(start, vector, container, distance_lookup):
    direction = vector[0]
    length = int(vector[1:])

    if direction == "R":
        for x in range(1, length+1):
            location = start[0] + x, start[1]
            container.add(location)
            fill_distance_lookup(start, location, x, distance_lookup)
        return start[0] + length, start[1]
    if vector.startswith('L'):
        for x in range(1, length+1):
            location = start[0] - x, start[1]
            container.add(location)
            fill_distance_lookup(start, location, x, distance_lookup)
        return start[0] - length, start[1]
    if vector.startswith('U'):
        for y in range(1, length+1):
            location = start[0], start[1] + y
            container.add(location)
            fill_distance_lookup(start, location, y, distance_lookup)
        return start[0], start[1] + length
    if vector.startswith('D'):
        for y in range(1, length+1):
            location = start[0], start[1] - y
            container.add(location)
            fill_distance_lookup(start, location, y, distance_lookup)
        return start[0], start[1] - length


def fill_distance_lookup(start, location, distance, distance_lookup):
    lookup = distance_lookup.get(location, None)
    if lookup is None:
        distance_lookup[location] = distance_lookup[start] + distance


if __name__ == '__main__':
    filename = 'input.txt'
    containers = []
    distance_lookups = []
    with open(filename, 'r') as fp:
        for index, line in enumerate(fp):
            start = (0, 0)
            container = set()
            distance_lookup = {start: 0}
            containers.append(container)
            distance_lookups.append(distance_lookup)
            vectors = line.split(',')
            for vector in vectors:
                start = generate(start, vector, container, distance_lookup)

    intersection_tuples = list(containers[0].intersection(containers[1]))
    intersections = map(lambda x: abs(x[0])+abs(x[1]), intersection_tuples)
    intersections = sorted(intersections)
    print(intersections[0])
