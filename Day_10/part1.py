def run():
    with open("input", "r") as input:
        adapters = input.read().splitlines()

        jolt_differences = {1: 0, 2: 0, 3: 0}

        # Sort strings by their numerical value
        adapters.sort(key=int)

        # Include first difference
        jolt_differences[int(adapters[0])] += 1

        for i in range(0, len(adapters) - 1):
            diff = int(adapters[i + 1]) - int(adapters[i])
            jolt_differences[diff] += 1

        # Include final adapter difference (always 3)
        jolt_differences[3] += 1

        print(f"Result: {jolt_differences[1] * jolt_differences[3]}")


if __name__ == "__main__":
    run()
