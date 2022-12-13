

def main():
    elves = []

    with open("day01_input.txt", "r") as f:
        txt = f.read()
        for txt_vals in txt.split("\n\n"):
            vals = [int(x) for x in txt_vals.strip().split("\n")]
            elves.append(vals)

    elves_sum = [sum(x) for x in elves]

    print(max(elves_sum))
    print(sum(sorted(elves_sum)[-3:]))


if __name__ == "__main__":
    main()
