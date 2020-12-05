import re

from functools import reduce

# Entry format: <lower>-<upper> <char>: <password>
entry_regex = "(\d+)-(\d+)\s(\w):\s([\w\d]+)"

def run():
    with open("input", "r") as input:
        entries = input.read().split("\n")[:-2]

    valid_count = 0

    for entry in entries:
        lowerStr, upperStr, target_char, password = re.match(entry_regex, entry).group(1,2,3,4)

        target_char_val = ord(target_char)
        lower = int(lowerStr) * target_char_val
        upper = int(upperStr) * target_char_val

        #print(target_char_val)
        #print(lower)
        #print(upper)
        #print(password)

        def char_sum_reducer(acc, char):
            if (char == target_char):
                return acc + target_char_val
            else:
                return acc

        char_sum = reduce(char_sum_reducer, password, 0)

        #print(char_sum)

        if char_sum >= lower and char_sum <= upper:
            valid_count += 1


    print(f"Solution: {valid_count}")

if __name__ == "__main__":
    run()
