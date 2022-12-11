import numpy as np
import math


def show(center, head, tail):
    vector_head = head - center
    vector_tail = tail - center
    n = 7
    n_half = n // 2
    for y in range(n):
        for x in range(n):
            if x == n_half + vector_head[0] and y == n_half + vector_head[1]:
                print("H", end="")
            elif x == n_half + vector_tail[0] and y == n_half + vector_tail[1]:
                print("T", end="")
            else:
                print(".", end="")
        print("")


def run_moves(moves):
    lookup_delta = {
        "U": np.array((0, 1), np.int32),
        "D": np.array((0, -1), np.int32),
        "L": np.array((-1, 0), np.int32),
        "R": np.array((1, 0), np.int32)
    }
    head = np.array((0, 0), np.int32)
    tail = np.array((0, 0), np.int32)

    pos_visited = {(tail[0], tail[1])}

    for key, dist in moves:
        delta = lookup_delta[key] * dist
        head_center = np.copy(head)
        show(head_center, head, tail)
        head += delta
        vector = head - tail
        length = np.sum(np.abs(vector))
        show(head_center, head, tail)
        if length == 0:
            continue
        elif length == 1:
            tail += vector
        elif length == 2:
            if vector[0] == 0 or vector[1] == 0:
                tail += vector//2
            else:
                tail += vector
        else:
            for i in range(2):
                if vector[i] != 0:
                    vector[i] /= abs(vector[i])
            tail += vector
        pos_visited.add((tail[0], tail[1]))
    return pos_visited


def main():
    moves = []
    with open("day9_input.txt", "r") as f:
        for line in f.readlines():
            key_txt, dist_txt = line.split(" ")
            moves.append((key_txt, int(dist_txt)))
    pos_visited = run_moves(moves)
    print(len(pos_visited))
    # print(moves[:20])


if __name__ == "__main__":
    main()
