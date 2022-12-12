
class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.n = len(instructions)
        self.counter = 0
        self.cycle = 0
        self.x = 1
        self.signal_strengths = []
        self.pixels = []
        for i in range(6):
            self.pixels.append(["." for _ in range(40)])
        # kick off cycling, needed for pixel 1
        self.incr_cycle()

    def step(self):
        opcode, param = self.instructions[self.counter]

        if opcode == "noop":
            self.incr_cycle()
        elif opcode == "addx":
            self.incr_cycle()
            self.x += param
            self.incr_cycle()

        self.counter += 1

        return self.counter < self.n

    def incr_cycle(self):
        self.cycle += 1

        i = (self.cycle - 1) // 40
        j = (self.cycle - 1) % 40
        if self.x <= (j+1) <= self.x+2:
            self.pixels[i][j] = "#"

        if self.cycle == 20 or (self.cycle > 20 and (self.cycle - 20) % 40 == 0):
            self.signal_strengths.append(self.cycle * self.x)


def main():
    instructions = []
    with open("day10_input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            args = line.split(" ")
            opcode = args[0]
            if len(args) == 2:
                param = int(args[1])
            else:
                param = None
            instructions.append((opcode, param))
    machine = CPU(instructions)
    while machine.step():
        pass
    print(sum(machine.signal_strengths))

    for line in machine.pixels:
        for letter in line:
            print(letter, end="")
        print("")


if __name__ == "__main__":
    main()
