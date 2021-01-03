class Ship():
    def __init__(self):
        self.rotation = 90
        self.x = 0
        self.y = 0

        self.move_set = {
            "N": self._move_north,
            "E": self._move_east,
            "S": self._move_south,
            "W": self._move_west,
            "R": self._turn_right,
            "L": self._turn_left,
            "F": self._move_local,
            "B": self._move_local,
        }

        self.local_movement = {
            0: self._move_north,
            90: self._move_east,
            180: self._move_south,
            270: self._move_west,
        }

    def _move_east(self, amount):
        self.x += amount

    def _move_west(self, amount):
        self.x -= amount

    def _move_north(self, amount):
        self.y += amount

    def _move_south(self, amount):
        self.y -= amount

    def _move_local(self, amount):
        move_action = self.local_movement[self.rotation]

        move_action(amount)

    def _turn_left(self, deg):
        self.rotation = (self.rotation - deg) % 360

    def _turn_right(self, deg):
        self.rotation = (self.rotation + deg) % 360

    def navigate(self, instruction):
        move_action = self.move_set[instruction[0]]
        amount = int(instruction[1:])

        # print(move_action.__name__, amount)
        move_action(amount)
        # print("Now @", self.get_coordinates(), self.rotation)

    def get_coordinates(self):
        return (self.x, self.y)


def run():
    with open("input", "r") as input:
        instructions = input.read().splitlines()

        ship = Ship()

        for instruction in instructions:
            ship.navigate(instruction)

        x, y = ship.get_coordinates()

        print(f"Result: {abs(x) + abs(y)}")


if __name__ == "__main__":
    run()
