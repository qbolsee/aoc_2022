
def step_floodfill(heightmap, distances):
    pass


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
    



if __name__ == "__main__":
    main()
