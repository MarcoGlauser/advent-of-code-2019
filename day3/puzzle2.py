from day3.puzzle1 import generate

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
    intersections = map(lambda x: distance_lookups[0][x]+distance_lookups[1][x], intersection_tuples)
    intersections = sorted(intersections)
    print(intersections[0])
