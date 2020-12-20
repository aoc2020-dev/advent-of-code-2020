from collections import deque


def is_valid_sum(target_sum, number_sequence):
    seenNumbers = set()

    for numberStr in number_sequence:
        number = int(numberStr)
        diff = int(target_sum) - number

        if diff in seenNumbers:
            return True
        else:
            seenNumbers.add(number)

    return False


def get_encoding_error(number_sequence, preamble_length):
    if preamble_length > len(number_sequence):
        raise "Number sequence must be larger than preamble"

    number_window = deque(number_sequence[:preamble_length])

    for summed_number in number_sequence[preamble_length:]:
        if not is_valid_sum(summed_number, number_window):
            return summed_number

        # Shift the window by one position
        number_window.popleft()
        number_window.append(summed_number)


def run():
    with open("input", "r") as input:
        number_sequence = input.read().splitlines()

        error = get_encoding_error(number_sequence, 25)
        print(f"Result: {error}")


if __name__ == "__main__":
    run()
