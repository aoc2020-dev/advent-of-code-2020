from itertools import repeat
from multiprocessing import Pool

EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


def tick_row(index, layout):
    return RowSimulation(index, layout).tick()


class RowSimulation():
    def __init__(self, index, layout):
        self.row = layout[index]
        self.index = index

        self.layout = layout
        self.last_column = len(layout[0]) - 1
        self.last_row = len(layout) - 1

    def __is_occupied(self, x, y):
        if ((x >= 0) and (x <= self.last_column) and (y >= 0) and (y <= self.last_row)):
            return self.layout[y][x] == OCCUPIED_SEAT

        return False

    def __count_above(self, x):
        if self.index == 0:
            return 0

        above = self.index - 1

        return int(self.__is_occupied(x - 1, above) + self.__is_occupied(x, above) + self.__is_occupied(x + 1, above))

    def __count_besides(self, x):
        return (self.__is_occupied(x - 1, self.index) + self.__is_occupied(x + 1, self.index))

    def __count_below(self, x):
        if self.index == self.last_row:
            return 0

        below = self.index + 1

        return (self.__is_occupied(x - 1, below) + self.__is_occupied(x, below) + self.__is_occupied(x + 1, below))

    def __count_occupied_around(self, x):
        count = 0
        if self.index > 0:
            count += self.__count_above(x)

        if self.index < self.last_row:
            count += self.__count_below(x)

        return count + self.__count_besides(x)

    def tick(self):
        has_changed = False
        num_occupied_in_row = 0
        next_row = list()

        for x, tile in enumerate(self.row):
            if tile != FLOOR:
                num_occupied_around = self.__count_occupied_around(x)

                if tile == OCCUPIED_SEAT:
                    if num_occupied_around >= 4:
                        has_changed = True
                        next_row.append(EMPTY_SEAT)
                    else:
                        next_row.append(OCCUPIED_SEAT)
                        num_occupied_in_row += 1

                elif tile == EMPTY_SEAT:
                    if num_occupied_around == 0:
                        has_changed = True
                        next_row.append(OCCUPIED_SEAT)
                        num_occupied_in_row += 1
                    else:
                        next_row.append(EMPTY_SEAT)
            else:
                # Floor tiles have no effect
                next_row.append(FLOOR)

        return next_row, num_occupied_in_row, has_changed


class LayoutSimulation():
    def __init__(self, layout, num_workers, chunk_size):
        self.layout = layout
        self.num_rows = len(self.layout)
        self.num_workers = num_workers
        self.chunk_size = chunk_size

    def __tick_layout(self, pool):
        has_layout_changed = False
        num_occupied_in_layout = 0
        next_layout = list()

        # [(1, <layout>), (2, <layout>), (3, <layout>), ...]
        self.worker_args = list(zip(range(self.num_rows), repeat(self.layout)))

        # Start tasks
        row_results = pool.starmap(tick_row, self.worker_args, chunksize=self.chunk_size)

        # Aggregate results
        for next_row, num_occupied_in_row, has_row_changed in row_results:
            has_layout_changed = has_layout_changed or has_row_changed
            num_occupied_in_layout += num_occupied_in_row

            next_layout.append(next_row)

        return next_layout, num_occupied_in_layout, has_layout_changed

    def simulate_until_stable(self):
        has_changed = False

        with Pool(self.num_workers) as pool:
            while True:
                next_layout, num_occupied, has_changed = self.__tick_layout(pool)

                if not has_changed:
                    return num_occupied

                self.layout = next_layout


def run():
    with open("input", "r") as input:
        layout = input.read().splitlines()

        num_occupied_seats = LayoutSimulation(layout, 16, 16).simulate_until_stable()

        print(f"Result: {num_occupied_seats}")


if __name__ == "__main__":
    run()
