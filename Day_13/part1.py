import re
import math


def run():
    with open("input", "r") as input:
        schedule = input.read()

        matches = re.findall(r"\d+", schedule)

        target_time = int(matches[0])
        departure_frequencies = matches[1:]

        closest_freq = 0
        min_wait = 0
        earliest_departure = -1

        for freqstr in departure_frequencies:
            freq = int(freqstr)

            next_departure = freq * math.ceil(target_time / freq)

            if next_departure < earliest_departure or earliest_departure == -1:
                earliest_departure = next_departure
                closest_freq = freq
                min_wait = next_departure - target_time

        print(f"Result: {closest_freq * min_wait}")


if __name__ == "__main__":
    run()
