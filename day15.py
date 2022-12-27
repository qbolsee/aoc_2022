import re


def manhattan_dist(xy1, xy2):
    return sum(abs(x-y) for x, y in zip(xy1, xy2))


class Sensor:
    def __init__(self, xy, xy_beacon):
        self.xy = xy
        self.xy_beacon = xy_beacon
        self.dist = manhattan_dist(self.xy, self.xy_beacon)

    def range_at(self, y):
        dy = y - self.xy[1]
        if abs(dy) > self.dist:
            return None
        dx = self.dist - abs(dy)
        return self.xy[0]-dx, self.xy[0]+dx


class HorizontalLine:
    def __init__(self, x1, x2, touched = False):
        self.x1 = x1
        self.x2 = x2
        self.touched = touched

    def intersect(self, other):
        return (other.x1 - self.x2) * (other.x2 - self.x1) <= 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Line {self.x1} -> {self.x2}"

    def __len__(self):
        return 1 + self.x2 - self.x1

    def union(self, other):
        if not self.intersect(other):
            raise ValueError(f"No intersectin: {self}, {other}")
        return HorizontalLine(min(self.x1, other.x1), max(self.x2, other.x2), touched=self.touched or other.touched)


def simplify_lines(lines):
    done = False
    i = 0
    n_remaining = len(lines)

    while not done:
        l1 = lines[0]
        if l1.touched:
            # we've come full circle it seems, stop now
            done = True
            break
        l1.touched = True
        new_lines = []
        j = 1
        while j < len(lines):
            l2 = lines[j]
            if l1.intersect(l2):
                l1 = l1.union(l2)
            else:
                new_lines.append(l2)
            j += 1
        lines = new_lines + [l1]
    return lines


def main():
    sensors = []
    with open("day15_input.txt", "r") as f:
        for line in f.readlines():
            m = re.match(r"^Sensor at x=([\-\d]+), y=([\-\d]+): "
                         r"closest beacon is at x=([\-\d]+), y=([\-\d]+)$",
                         line.strip())
            if m is None:
                print(f"Cannot parse: '{line}'")
                continue
            xy = int(m.group(1)), int(m.group(2))
            xy_beacon = int(m.group(3)), int(m.group(4))
            sensors.append(Sensor(xy, xy_beacon))

    y_slice = 2000000

    ranges = list(s.range_at(y_slice) for s in sensors)

    lines = [HorizontalLine(*r) for r in ranges if r is not None]

    lines = simplify_lines(lines)

    len_lines = sum([len(x) for x in lines])

    set_x_beacon = set()

    for s in sensors:
        if s.xy_beacon[1] == y_slice:
            set_x_beacon.add(s.xy_beacon[0])

    print(len_lines - len(set_x_beacon))

    for y_slice in range(0, 1+4000000):
        ranges = list(s.range_at(y_slice) for s in sensors)
        lines = [HorizontalLine(*r) for r in ranges if r is not None]
        if len(lines) == 0:
            continue
        lines = simplify_lines(lines)

        if len(lines) == 2:
            # found 2 lines
            x_beacon = min(lines[0].x2, lines[1].x2)+1
            tuning = x_beacon * 4000000 + y_slice
            print(tuning)
            break


if __name__ == "__main__":
    main()
