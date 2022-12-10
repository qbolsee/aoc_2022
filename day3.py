
def priority(x):
    p = ord(x)
    if p >= ord("a"):
        return p - ord("a") + 1
    else:
        return p - ord("A") + 27


def main():
    compartments1 = []
    compartments2 = []
    sacks = []
    priority_total = 0
    with open("day3_input.txt", "r") as f:
        for line in f.readlines():
            txt = line.strip()
            n = len(txt)
            sacks.append(txt)
            compartments1.append(txt[:n//2])
            compartments2.append(txt[n//2:])
            set1 = set(compartments1[-1])
            set2 = set(compartments2[-1])
            set_inter = set1.intersection(set2)
            for x in set_inter:
                priority_total += priority(x)
                break

    print(priority_total)

    priority_total = 0
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]

    for g in groups:
        set1 = set(g[0])
        set2 = set(g[1])
        set3 = set(g[2])
        set_inter = set1.intersection(set2).intersection(set3)
        for x in set_inter:
            priority_total += priority(x)

    print(priority_total)


if __name__ == "__main__":
    main()
