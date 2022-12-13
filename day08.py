import numpy as np


def raycast_from_edge(trees, sign, columnwise=False):
    visible = np.zeros(trees.shape, bool)
    h, w = trees.shape
    if columnwise:
        trees = np.transpose(trees, (1, 0))
        h, w = w, h
    i = -1 if sign == -1 else 0
    row_max = -np.ones((w,), dtype=np.int32)
    for j in range(h):
        visible[i, :] = trees[i, :] > row_max
        row_max = np.maximum(trees[i, :], row_max)
        i += sign
    if columnwise:
        return np.transpose(visible, (1, 0))
    else:
        return visible


def raycast_from_tree(trees, ij):
    dists = np.zeros((4,), dtype=np.int32)

    ij = np.array(ij, dtype=np.int32)
    ij_init = np.copy(ij)

    height = trees[ij[0], ij[1]]

    h, w = trees.shape

    k = 0
    for ray in np.array([[1, 0],
                         [-1, 0],
                         [0, 1],
                         [0, -1]], dtype=np.int32):
        # reset
        dist = 0
        ij[:] = ij_init[:]
        ij += ray
        while (0 <= ij[0] <= h-1) and (0 <= ij[1] <= w-1):
            dist += 1
            if dist > 0 and trees[ij[0], ij[1]] >= height:
                break
            ij += ray
        dists[k] = dist
        k += 1
    return np.prod(dists)


def main():
    m = []
    with open("day08_input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            m.append([int(x) for x in line])
    m = np.array(m, np.int32)
    h, w = m.shape

    # max along all rows
    visible_up = raycast_from_edge(m, 1, False)
    visible_down = raycast_from_edge(m, -1, False)
    visible_left = raycast_from_edge(m, 1, True)
    visible_right = raycast_from_edge(m, -1, True)

    visible = visible_up | visible_down | visible_left | visible_right

    for i in range(h):
        print("".join([str(x) for x in visible[i, :].astype(np.int32)]))

    print(np.sum(visible))

    max_score = 0
    for i in range(1, h-1):
        for j in range(1, w-1):
            score = raycast_from_tree(m, (i, j))
            max_score = max(score, max_score)
    print(max_score)


if __name__ == "__main__":
    main()
