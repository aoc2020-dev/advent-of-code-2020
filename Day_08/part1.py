def run():
    with open("input", "r") as input:
        instructions = input.read().splitlines()

        visited_indicies = set()
        acc = 0
        pc = 0
        while pc not in visited_indicies:
            visited_indicies.add(pc)
            instruction = instructions[pc]

            op, arg = instruction.split(" ")

            if op == "jmp":
                pc += int(arg)
            elif op == "acc":
                acc += int(arg)
                pc += 1
            else:
                pc += 1

        print(f"Result: {acc}")


if __name__ == "__main__":
    run()
