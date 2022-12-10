import re


def move_crates(piles, moves, flip=True):
    piles = piles.copy()
    for m in moves:
        amount, s, e = m
        items = piles[s - 1][:amount]
        if flip:
            items = items[::-1]
        piles[e - 1] = items + piles[e - 1]
        piles[s - 1] = piles[s - 1][amount:]
    return piles


def main():
    n = 9
    piles = [[] for _ in range(n)]

    with open("day5_input.txt", "r") as f:
        section = 0
        moves = []
        for line in f.readlines():
            line = line.strip()
            if section == 0:
                if line[0] != "[":
                    section = 1
                    continue
                i = 0
                k = 0
                while i < len(line):
                    letter = line[i + 1:i + 2]
                    if letter != " ":
                        piles[k] = piles[k] + [letter]
                    i += 4
                    k += 1
            if section == 1:
                section = 2
            if section == 2:
                m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
                if m is None:
                    continue
                moves.append([int(m.group(1+k)) for k in range(3)])
        piles1 = move_crates(piles, moves, True)
        piles2 = move_crates(piles, moves, False)

        result1 = ""
        result2 = ""
        for p1, p2 in zip(piles1, piles2):
            if len(p1) > 0:
                result1 += p1[0]
            if len(p2) > 0:
                result2 += p2[0]

        print(result1)
        print(result2)


if __name__ == "__main__":
    main()
