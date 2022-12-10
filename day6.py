

def main():
    with open("day6_input.txt", "r") as f:
        txt = f.readline().strip()
        i = 4
        while i < len(txt):
            txt_slice = txt[i:i+4]
            txt_set = set(txt_slice)
            if len(txt_set) == 4:
                break
            i += 1
        s = i+4

        print(s)

        i = s
        while i < len(txt):
            txt_slice = txt[i:i+14]
            txt_set = set(txt_slice)
            if len(txt_set) == 14:
                break
            i += 1
        m = i + 14

        print(m)




if __name__ == "__main__":
    main()
