from __future__ import annotations
from typing import Tuple, Set
import itertools


class Octopus:
    position: Tuple[int, int]
    value: int
    neighbours: Set[Octopus]
    flashed: bool

    def __init__(self, position, value):
        self.position = position
        self.value = value

    def __hash__(self):
        return self.position.__hash__()

    # def __repr__(self):
    #     return f"({self.x},{self.y},{self.value})"

    def can_flash(self):
        return not self.flashed

    def __repr__(self):
        return f"({self.value})"


def main():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    octopus_grid = parse_input(input_file)
    round_count = 100
    flash_count = 0
    for _ in range(round_count):
        __vis_grid(octopus_grid)
        octopus_grid, flash_count_this_round = do_step(octopus_grid)
        flash_count += flash_count_this_round
    print(f"After [{round_count}] rounds there were [{flash_count}] flashes")


def __vis_grid(grid):
    print("\n".join(["".join([str(a) for a in row]) for row in grid]))


def do_step(octopus_grid):
    flashing_octopi = []
    for row in octopus_grid:
        for octopus in row:
            octopus.value += 1
            octopus.flashed = False
            if octopus.value > 9:
                flashing_octopi.append(octopus)

    still_to_flash_octopii = flashing_octopi
    flash_count = 0

    while still_to_flash_octopii:
        flashing_octopus = still_to_flash_octopii.pop(0)
        if not flashing_octopus.can_flash():
            continue

        flashing_octopus.flashed = True
        flash_count += 1
        flashing_octopus.value = 0
        for neighbour in flashing_octopus.neighbours:
            if neighbour.can_flash():
                neighbour.value += 1
                if neighbour.value > 9:
                    still_to_flash_octopii.append(neighbour)
    return octopus_grid, flash_count


def get_neighbours(octopus, grid):
    neighbour_shifts = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    neighbour_shifts.remove((0, 0))
    neighbours = set()
    for shift in neighbour_shifts:
        x_neighbour, y_neighbour = map(lambda x, y: x + y, shift, octopus.position)
        if x_neighbour in range(len(grid[0])) and y_neighbour in range(len(grid)):
            neighbours.add(grid[x_neighbour][y_neighbour])
    return neighbours


def parse_input(input_file):
    with open(input_file) as file:
        grid = [
            [
                Octopus((row_idx, col_idx), int(octopus))
                for col_idx, octopus in enumerate(line.strip())
            ]
            for row_idx, line in enumerate(file)
        ]
        for row in grid:
            for octopus in row:
                octopus.neighbours = get_neighbours(octopus, grid)
        return grid


if __name__ == "__main__":
    main()
