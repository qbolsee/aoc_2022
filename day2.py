def main():
    lookup_game = {(0, 1): 1,
                   (0, 2): 0,
                   (1, 2): 1,
                   (1, 0): 0,
                   (2, 0): 1,
                   (2, 1): 0}

    lookup_win = {
        0: 1,
        1: 2,
        2: 0
    }
    lookup_lose = {
        0: 2,
        1: 0,
        2: 1
    }

    score = 0
    score2 = 0
    with open("day2_input.txt", "r") as f:
        for line in f.readlines():
            letter1, letter2 = line.strip().split(" ")
            ind1 = ord(letter1) - ord("A")
            ind2 = ord(letter2) - ord("X")
            score += ind2 + 1
            if ind1 == ind2:
                win = 3
            else:
                win = lookup_game[ind1, ind2] * 6
            score += win
            if ind2 == 0:
                # need to lose
                ind2_corr = lookup_lose[ind1]
                win2 = 0
            elif ind2 == 2:
                # need to win
                ind2_corr = lookup_win[ind1]
                win2 = 6
            else:
                # draw
                ind2_corr = ind1
                win2 = 3

            score2 += ind2_corr + 1
            score2 += win2

    print(score)
    print(score2)


if __name__ == "__main__":
    main()
