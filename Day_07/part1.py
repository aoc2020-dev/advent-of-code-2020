import re

delimeter = " contain "
color_pattern = r"(?:\d+ )?(\w+ \w+ \w+)"


def unpack_all_bags(current_bag, reverse_bag_dict, unpacked_bags=dict()):
    # Bag has no parent so return it
    if current_bag not in reverse_bag_dict:
        return []

    next_bags = reverse_bag_dict[current_bag]
    containing_bags = list()

    for bag in next_bags:
        if bag not in unpacked_bags:
            unpacked_bags[bag] = True
            containing_bags.append(bag)
            containing_bags += unpack_all_bags(bag, reverse_bag_dict, unpacked_bags)

    return containing_bags


def run():
    with open("input", "r") as input:
        entries = input.read().splitlines()

        reverse_color_dict = dict()

        for entry in entries:
            containing_color, contained_color_desc = entry.split(delimeter)

            contained_colors = re.findall(color_pattern, contained_color_desc)

            for color in contained_colors:
                color_key = color[:-1] if color[-1] == "s" else color
                containing_color_value = containing_color[:-1]

                if color_key in reverse_color_dict:
                    reverse_color_dict[color_key].append(containing_color_value)
                else:
                    reverse_color_dict[color_key] = [containing_color_value]

        final_bags = unpack_all_bags("shiny gold bag", reverse_color_dict)

        print(f"Result {len(final_bags)}")


if __name__ == "__main__":
    run()
