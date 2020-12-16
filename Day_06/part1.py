import re

delimiter = "\n\n"

def run():
    with open("input", "r") as input:
        entries = input.read().split(delimiter)

        total = 0

        for group_answers in entries:
            seen_answers = dict()
            group_count = 0

            for answer in group_answers: 

                if answer != "\n" and not answer in seen_answers:
                    group_count += 1
                    seen_answers[answer] = True

            total += group_count
       
        print(f"Result: {total}")

if __name__ == "__main__":
    run()
