from collections import defaultdict


def neighbors_ij(i, j):
    neighbors = set()
    for di, dj in [[-1, 0],
                   [1, 0],
                   [0, -1],
                   [0, 1]]:
        neighbors.add((i+di, j+dj))
    return neighbors


def solve_floodfill(heightmap, seeds, exit):
    h = len(heightmap)
    w = len(heightmap[0])

    dist_max = h * w

    distances = defaultdict(lambda: -1)
    for i in range(h):
        for j in range(w):
            distances[i, j] = dist_max

    for i, j in seeds:
        distances[i, j] = 0

    while len(seeds) > 0:
        seeds = step_floodfill(heightmap, distances, seeds, dist_max)

    return distances[exit]


def step_floodfill(heightmap, distances, seeds, dist_max):
    new_seeds = set()
    for i, j in seeds:
        d = distances[i, j]
        h = ord(heightmap[i][j])
        for i2, j2 in neighbors_ij(i, j):
            d2 = distances[i2, j2]
            if d2 == -1:
                continue
            h2 = ord(heightmap[i2][j2])
            if h2-1 <= h and d2 == dist_max:
                distances[i2, j2] = d+1
                new_seeds.add((i2, j2))
    return new_seeds


def main():
    heightmap = []
    with open("day12_input.txt", "r") as f:
        for line in f.readlines():
            heightmap.append([x for x in line.strip()])

    h = len(heightmap)
    w = len(heightmap[0])

    start = (0, 0)
    exit = (0, 0)

    for i in range(h):
        for j in range(w):
            if heightmap[i][j] == "S":
                start = i, j
                heightmap[i][j] = "a"
            elif heightmap[i][j] == "E":
                exit = i, j
                heightmap[i][j] = "z"

    seeds1 = {start}
    dist1 = solve_floodfill(heightmap, seeds1, exit)
    print(dist1)

    seeds2 = set()

    for i in range(h):
        for j in range(w):
            if heightmap[i][j] == "a":
                seeds2.add((i, j))
    dist2 = solve_floodfill(heightmap, seeds2, exit)
    print(dist2)


if __name__ == "__main__":
    main()
