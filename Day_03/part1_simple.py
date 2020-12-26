tree_token = "#"
steps_per_row = 3


def run():
    with open("input", "r") as input:
        tree_map = input.read().splitlines()

        total_tree_count = 0
        width = len(tree_map[0])

        print(width)

        print(tree_map[0][:-1])
        for y in range(1, len(tree_map)):
            x = (y * steps_per_row) % width

            if tree_map[y][x] == tree_token:
                total_tree_count += 1

        print(f"Result: {total_tree_count}")


if __name__ == "__main__":
    run()
