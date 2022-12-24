import functools


def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


def compare(l, r):
    if isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    if isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    if isinstance(l, int) and isinstance(r, int):
        # -1 if l < r
        return sign(l - r)
    # list and list
    len_l = len(l)
    len_r = len(r)
    len_min = min(len_l, len_r)
    for i in range(len_min):
        val = compare(l[i], r[i])
        if val != 0:
            return val
    return sign(len_l - len_r)


def main():
    pairs = []
    with open("day13_input.txt", "r") as f:
        pair = []
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            pair.append(eval(line))
            if len(pair) == 2:
                pairs.append(pair)
                pair = []

    n = len(pairs)
    correct_order = []
    for l, r in pairs:
        correct_order.append(compare(l, r) < 0)

    print(sum([i+1 for i in range(n) if correct_order[i]]))

    packets = []
    for p1, p2 in pairs:
        packets.append(p1)
        packets.append(p2)

    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=functools.cmp_to_key(compare))

    ind1 = packets.index([[2]])+1
    ind2 = packets.index([[6]])+1

    print(ind1 * ind2)


if __name__ == "__main__":
    main()
