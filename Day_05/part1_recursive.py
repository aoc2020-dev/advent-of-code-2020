def parse(lo, hi, sequence, lo_token):
    if lo == hi:
        return lo

    lo_mid = lo + ((hi - lo) >> 1)
    remaining_sequence = sequence[1:]

    if sequence[0] == lo_token:
        return parse(lo, lo_mid, remaining_sequence, lo_token)
    else:
        return parse(lo_mid + 1, hi, remaining_sequence, lo_token)


def parse_row(sequence):
    return parse(0, 127, sequence[0:7], "F")


def parse_column(sequence):
    return parse(0, 7, sequence[7:], "L")


def run():
    with open("input", "r") as input:
        highest_id = -1
        entries = input.read().splitlines()

        for entry in entries:
            row = parse_row(entry)
            column = parse_column(entry)

            seat_id = (row << 3) + column

            if seat_id > highest_id:
                highest_id = seat_id

        print(f"Result: {highest_id}")


if __name__ == "__main__":
    run()
