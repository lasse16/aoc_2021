class Cave:
    def __init__(self, name):
        self.name = name
        self.small = name.islower()
        self.neighbours = []

    def get_neighbours(self):
        return self.neighbours

    def is_small(self):
        return self.small

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def __repr__(self):
        return self.name


def main():
    input_file = "input.txt"
    caves = parse_input(input_file)
    caves = prune_dead_ends(caves)
    # Cant figure out a way for backward generation with the small cave constraint
    paths = forward_generate_paths(caves)
    print(len(paths))


def forward_generate_paths(caves):
    completed_paths = []
    paths = []
    start_node = [cave for cave in caves if cave.name == "start"][0]
    end_node = [cave for cave in caves if cave.name == "end"][0]
    paths.append([start_node])
    while paths:
        path = paths[0]
        current_node = path[-1]
        neighbours = current_node.get_neighbours()
        for neighbour in neighbours:
            if neighbour.is_small() and neighbour in path:
                continue

            path_copy = path.copy()
            path_copy.append(neighbour)
            if neighbour == end_node:
                completed_paths.append(path_copy)
            else:
                paths.append(path_copy)
        paths.remove(path)
    return completed_paths


def prune_dead_ends(caves):
    dead_ends = []
    for cave in caves:
        neighbours = cave.get_neighbours()
        if len(neighbours) == 1 and neighbours[0].is_small():
            dead_ends.append(cave)
            neighbours[0].neighbours.remove(cave)
    for cave in dead_ends:
        caves.remove(cave)
    return caves


def parse_input(input_file):
    caves = {}
    with open(input_file) as file:
        for line in file:
            connected_cave_names = line.strip().split("-")
            name1 = connected_cave_names[0]
            cave1 = caves.get(name1, Cave(name1))

            name2 = connected_cave_names[1]
            cave2 = caves.get(name2, Cave(name2))

            cave2.neighbours.append(cave1)
            cave1.neighbours.append(cave2)
            caves[name1] = cave1
            caves[name2] = cave2

    return list(caves.values())


if __name__ == "__main__":
    main()
