import re
import copy


def parse_int(pattern, line):
    m = re.match(pattern, line)
    if m is None:
        return None
    return int(m.group(1))


def parse_str(pattern, line):
    m = re.match(pattern, line)
    if m is None:
        return None
    return m.group(1)


class Monkey:
    def __init__(self, lines):
        self.index = parse_int(r"^Monkey (\d+):$", lines[0])
        txt_items = parse_str(r"^  Starting items: (.+)$", lines[1])
        self.items = [int(x.strip()) for x in txt_items.split(",")]
        self.operation = parse_str(r"^  Operation: new = (.+)$", lines[2])
        self.test_divisible = parse_int(r"^  Test: divisible by (\d+)$", lines[3])
        self.test_true_index = parse_int(r"^    If true: throw to monkey (\d+)$", lines[4])
        self.test_false_index = parse_int(r"^    If false: throw to monkey (\d+)$", lines[5])
        self.inspect_count = 0


def get_monkey_business(monkeys):
    counts_sorted = sorted([m.inspect_count for m in monkeys.values()])
    monkey_business = counts_sorted[-1] * counts_sorted[-2]
    return monkey_business


def round(monkeys, divide_by_three=True, modulo_divide=None):
    n_monkeys = len(monkeys)

    for i in range(n_monkeys):
        m = monkeys[i]
        while m.items:
            m.inspect_count += 1
            old = m.items.pop(0)
            worry = eval(m.operation)
            if divide_by_three:
                worry //= 3
            if modulo_divide is not None:
                worry %= modulo_divide
            if worry % m.test_divisible == 0:
                i_other = m.test_true_index
            else:
                i_other = m.test_false_index
            monkeys[i_other].items.append(worry)


def main():
    monkeys = {}
    with open("day11_input.txt", "r") as f:
        lines = f.readlines()
        n = len(lines)
        for i in range(0, n, 7):
            m = Monkey(lines[i:i+6])
            monkeys[m.index] = m

        monkeys_backup = copy.deepcopy(monkeys)

        for k in range(20):
            round(monkeys)

        print(get_monkey_business(monkeys))

        modulo_divide = 1
        for m in monkeys_backup.values():
            modulo_divide *= m.test_divisible

        for k in range(10000):
            round(monkeys_backup, False, modulo_divide)

        print(get_monkey_business(monkeys_backup))


if __name__ == "__main__":
    main()
