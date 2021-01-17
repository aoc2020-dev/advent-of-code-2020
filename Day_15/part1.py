def run():
    # reference_numbers = [0, 3, 6]
    input_numbers = [8, 0, 17, 4, 1, 12]

    starting_numbers = input_numbers
    spoken_numbers = dict()

    for turn, num in enumerate(starting_numbers, start=1):
        spoken_numbers[num] = [turn]

    last_spoken_number = starting_numbers[-1]

    for i in range(len(starting_numbers) + 1, 2020 + 1):
        spoken_at_turns = spoken_numbers[last_spoken_number]

        next_spoken_number = spoken_at_turns[-1] - spoken_at_turns[-2] if len(spoken_at_turns) > 1 else 0

        if next_spoken_number not in spoken_numbers:
            spoken_numbers[next_spoken_number] = [i]
        else:
            spoken_numbers[next_spoken_number].append(i)

        last_spoken_number = next_spoken_number

    print(f"Result: {last_spoken_number}")


if __name__ == "__main__":
    run()
