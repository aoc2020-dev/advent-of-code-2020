import re


def merge_intervals(intervals):
    sorted(intervals, key=lambda i: i[0])

    merged_intervals = list()

    merged_intervals.append(intervals[0])

    for current_interval in intervals[1:]:

        last_interval = merged_intervals[-1]

        if (last_interval[1] >= current_interval[0]):
            merged = (min(last_interval[0], current_interval[0]), max(last_interval[1], current_interval[1]))
            merged_intervals.pop()
            merged_intervals.append(merged)
        else:
            merged_intervals.append(current_interval)

    return [range(lo, hi + 1) for (lo, hi) in merged_intervals]


def is_in_ranges(value, ranges):
    for r in ranges:
        if value in r:
            return True

    return False


def run():
    with open("input", "r") as input:
        ranges, my_ticket, nearby_tickets = input.read().split("\n\n")

        intervals = [(int(lo), int(hi)) for (lo, hi) in re.findall(r"(\d+)-(\d+)", ranges)]

        merged_intervals = merge_intervals(intervals)

        invalid_fields = list()

        ticket_values = [int(v) for v in re.findall(r"\d+", nearby_tickets)]

        for value in ticket_values:
            if not is_in_ranges(value, merged_intervals):
                invalid_fields.append(value)

        print(f"Result {sum(invalid_fields)}")


if __name__ == "__main__":
    run()
