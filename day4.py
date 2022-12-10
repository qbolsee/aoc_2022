

def main():
    n1 = 0
    n2 = 0
    with open("day4_input.txt", "r") as f:
        for line in f.readlines():
            range1, range2 = line.strip().split(",")
            s1, e1 = [int(x) for x in range1.split("-")]
            s2, e2 = [int(x) for x in range2.split("-")]
            if (s1 - s2) * (e1 - e2) <= 0:
                n1 += 1
            if (s2-e1) * (e2-s1) <= 0:
                n2 += 1

    print(n1)
    print(n2)


if __name__ == "__main__":
    main()
