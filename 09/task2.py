from dataclasses import dataclass
import math
from queue import SimpleQueue


@dataclass
class CaveTile:
    x: int
    y: int
    height: int

    def __hash__(self):
        return self.x ** 2 + self.y


def main():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    cave_tiles = parse_input(input_file)
    lowpoints = find_lowpoints(cave_tiles)
    basins = flood_basins(cave_tiles, lowpoints)
    basins = sorted(basins, key=lambda x: len(x), reverse=True)
    print(math.prod([len(basin) for basin in basins[:3]]))


def flood_basins(tiles, lowpoints):
    basins = {point: [point] for point in lowpoints}

    # NO NEED TO COMPARE DISTANCES TO LOWPOINTS AS PER INSTRUCTION
    # " ALL POINTS BELONG TO ONLY ONE BASIN AT ANY TIME"
    # Do BFS from each lowpoint until no new neighbours are visited
    for point in lowpoints:
        basin = basins[point]
        visiting_queue = [point]
        while visiting_queue:
            current_node = visiting_queue.pop(0)
            for neighbour in get_neighbours(current_node.x, current_node.y, tiles):
                if neighbour not in basin and neighbour.height != 9:
                    basin.append(neighbour)
                    visiting_queue.append(neighbour)

    return basins.values()


def parse_input(input_file):
    with open(input_file) as file:
        return [[int(char_) for char_ in line.strip()] for line in file]


def find_lowpoints(tiles):
    lowpoints = []
    for row_idx, row in enumerate(tiles):
        for col_idx, point in enumerate(row):
            neighbours = get_neighbours(row_idx, col_idx, tiles)
            if all(neighbour.height > point for neighbour in neighbours):
                lowpoints.append(CaveTile(row_idx, col_idx, point))
    return lowpoints


def get_neighbours(row, col, tiles):
    neighbours = []
    for row_shift, col_shift in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        row_neighbour = row + row_shift
        col_neighbour = col + col_shift
        if row_neighbour in range(len(tiles)) and col_neighbour in range(len(tiles[0])):
            neighbours.append(
                CaveTile(
                    row_neighbour, col_neighbour, tiles[row_neighbour][col_neighbour]
                )
            )
    return neighbours


if __name__ == "__main__":
    main()
