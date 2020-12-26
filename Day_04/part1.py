import re

separator = "\n\n"
required_pattern = r"byr|iyr|eyr|hgt|hcl|ecl|pid"
num_required_fields = 7


def run():
    with open("input", "r") as input:
        entries = input.read().split(separator)

        total_valid_count = 0

        for e in entries:
            matches = re.findall(required_pattern, e)

            if len(matches) >= num_required_fields:
                total_valid_count += 1

        print(f"Result: {total_valid_count}")


if __name__ == "__main__":
    run()
