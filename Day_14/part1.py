import re

mem_pattern = r"mem\[(\d+)\] = (\d+)"


def run():
    with open("input", "r") as input:
        instructions = input.read().splitlines()

        memory = dict()
        mask = ""

        for ins in instructions:
            if ins.startswith("me"):
                addressStr, valueStr = re.match(mem_pattern, ins).group(1, 2)

                value_bits = bin(int(valueStr))[2:].zfill(36)

                masked_value_bits = list()

                for index, bit in enumerate(mask):
                    if bit != "X":
                        masked_value_bits.append(bit)
                    else:
                        masked_value_bits.append(value_bits[index])

                memory[addressStr] = int("".join(masked_value_bits), 2)

            elif ins.startswith("ma"):
                mask = ins.split("= ")[1]

        memorySum = sum(memory.values())

        print(f"Result: {memorySum}")


if __name__ == "__main__":
    run()
