import numpy as np
import os
import time


def show(center, head, tails):
    n_tails, _ = tails.shape
    vector_head = head - center
    n = 21
    n_half = n // 2
    for y in range(n):
        for x in range(n):
            found_match = False
            if x == n_half + vector_head[0] and y == n_half + vector_head[1]:
                print("H", end="")
                found_match = True
            if not found_match:
                for t_index in range(n_tails):
                    vector_tail = tails[t_index] - center
                    if x == n_half + vector_tail[0] and y == n_half + vector_tail[1]:
                        print(1+t_index if n_tails > 1 else "T", end="")
                        found_match = True
                        break
            if not found_match:
                print(".", end="")
        print("")


def run_moves(moves, n_tails=1, show_grid=False):
    lookup_delta = {
        "U": np.array((0, 1), np.int32),
        "D": np.array((0, -1), np.int32),
        "L": np.array((-1, 0), np.int32),
        "R": np.array((1, 0), np.int32)
    }
    head = np.zeros((2,), np.int32)
    tails = np.zeros((n_tails, 2), np.int32)

    pos_visited = {(0, 0)}

    for key, dist in moves:
        if show_grid:
            print(key, dist)
        delta = lookup_delta[key]
        head_center = np.copy(head)
        for k in range(dist):
            for t_index in range(n_tails):
                if t_index == 0:
                    h = head
                    h += delta
                else:
                    h = tails[t_index-1]
                # if show_grid:
                #     show(head_center, head, tails)
                #     print("---")
                vector = h - tails[t_index]
                length = np.sum(np.abs(vector))
                # if show_grid:
                #     show(head_center, head, tails)
                #     print("+++")
                if length <= 1:
                    continue
                elif length == 2:
                    if vector[0] == 0 or vector[1] == 0:
                        tails[t_index, :] += vector//2
                    else:
                        continue
                else:
                    for i in range(2):
                        if vector[i] != 0:
                            vector[i] /= abs(vector[i])
                    tails[t_index, :] += vector
            pos_visited.add((tails[-1, 0], tails[-1, 1]))
            if show_grid:
                os.system("cls")
                show(head_center, head, tails)
                print("===")
                time.sleep(0.1)
    return pos_visited


def main():
    moves = []
    with open("day09_input.txt", "r") as f:
        for line in f.readlines():
            key_txt, dist_txt = line.split(" ")
            moves.append((key_txt, int(dist_txt)))
    pos_visited = run_moves(moves, show_grid=False)
    print(len(pos_visited))
    pos_visited = run_moves(moves, 9, show_grid=False)
    print(len(pos_visited))
    # print(moves[:20])


if __name__ == "__main__":
    main()
