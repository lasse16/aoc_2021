def main():
    input_file = "input.txt"
    cave_tiles = parse_input(input_file)
    lowpoints = find_lowpoints(cave_tiles)
    print(len(lowpoints) + sum([point[2] for point in lowpoints]))


def parse_input(input_file):
    with open(input_file) as file:
        return [[int(char_) for char_ in line.strip()] for line in file]


def find_lowpoints(tiles):
    lowpoints = []
    for row_idx, row in enumerate(tiles):
        for col_idx, point in enumerate(row):
            neighbours = get_neighbours(row_idx, col_idx, tiles)
            if all(neighbour > point for neighbour in neighbours):
                lowpoints.append((row_idx, col_idx, point))
    return lowpoints


def get_neighbours(row, col, tiles):
    neighbours = []
    for row_shift, col_shift in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        row_neighbour = row + row_shift
        col_neighbour = col + col_shift
        if row_neighbour in range(len(tiles)) and col_neighbour in range(len(tiles[0])):
            neighbours.append(tiles[row_neighbour][col_neighbour])
    return neighbours


if __name__ == "__main__":
    main()
