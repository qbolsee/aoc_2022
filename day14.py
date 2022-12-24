import numpy as np
import math
import sys
import cv2


CELL_EMPTY = 0
CELL_WALL = 1
CELL_SAND = 2


def add_sand(scan, origin=(500, 0)):
    h, w = scan.shape

    x = origin[0]
    y = origin[1]

    blocked = False
    endless_fall = False

    def is_in_bounds(coord):
        return 0 <= coord[0] <= w-1 and 0 <= coord[1] <= h-1

    while not blocked and not endless_fall:
        blocked = True
        for delta in [[0, 1],
                      [-1, 1],
                      [1, 1]]:
            x_go, y_go = x + delta[0], y + delta[1]
            if not is_in_bounds((x_go, y_go)):
                endless_fall = True
                blocked = False
                break
            if scan[y_go, x_go] == CELL_EMPTY:
                x, y = x_go, y_go
                blocked = False
                break
        if blocked:
            scan[y, x] = CELL_SAND

    return endless_fall


def print_scan(scan):
    h, w = scan.shape
    dict_visual = {
        CELL_EMPTY: ".",
        CELL_WALL: "#",
        CELL_SAND: "O"
    }
    for i in range(h):
        for j in range(w):
            print(dict_visual[scan[i][j]], end="")
        print("")


def main():
    w = 0
    h = 0
    walls = []
    with open("day14_input.txt") as f:
        for line in f.readlines():
            wall = []
            for item in line.strip().split(" -> "):
                x, y = [int(a) for a in item.split(",")]
                wall.append((x, y))
                w = max(x, w)
                h = max(y, h)

            walls.append(wall)

    h = h + 1
    w = w + 1
    scan = np.zeros((h, w), dtype=np.int32)
    for wall in walls:
        for k in range(len(wall)-1):
            x1, y1 = wall[k]
            x2, y2 = wall[k+1]
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            if x1 == x2:
                scan[y1:y2+1, x1] = CELL_WALL
            else:
                scan[y1, x1:x2+1] = CELL_WALL

    scan_backup = np.copy(scan)
    endless_fall = False

    while not endless_fall:
        endless_fall = add_sand(scan)
    print(np.sum(scan == CELL_SAND))

    # enough padding for the bottom layer and surely not overflowing from the sides
    scan = np.pad(scan_backup, ((0, 2), (h, h)))
    scan[-1, :] = CELL_WALL

    origin_offset = (500+h, 0)

    scan_img = np.zeros(scan.shape, dtype=np.uint8)

    display = True

    endless_fall = False
    first_show = True
    while not endless_fall:
        # print_scan(scan[:, 494:])
        endless_fall = add_sand(scan, origin=origin_offset)

        scan_img[scan == CELL_EMPTY] = 0
        scan_img[scan == CELL_WALL] = 127
        scan_img[scan == CELL_SAND] = 255

        if display:
            scan_show = scan_img[:, 500:]
            h_show, w_show = scan_show.shape
            scan_show = cv2.resize(scan_show, (w_show*4, h_show*4), interpolation=cv2.INTER_NEAREST)
            cv2.imshow('Frame', scan_show)
            if cv2.waitKey(10000 if first_show else 1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                display = False
            first_show = False

        if scan[origin_offset[1], origin_offset[0]] == CELL_SAND:
            break

    cv2.destroyAllWindows()

    print(np.sum(scan == CELL_SAND))


if __name__ == "__main__":
    main()
