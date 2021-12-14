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


class Path:
    def __init__(self, start):
        self.nodes = [start]
        self.double_visited_small = False

    def append(self, node):
        if node.is_small() and node in self:
            self.double_visited_small = True

        self.nodes.append(node)

    def get_last_node(self):
        return self.nodes[-1]

    def copy(self):
        copy_obj = Path(self.nodes[0])
        copy_obj.nodes = self.nodes.copy()
        copy_obj.double_visited_small = self.double_visited_small
        return copy_obj

    def __eq__(self, other):
        return (
            self.nodes == other.nodes
            and self.double_visited_small == other.double_visited_small
        )

    def __iter__(self):
        return iter(self.nodes)

    def __repr__(self):
        return str(self.nodes)

    def __contains__(self, item):
        return item in self.nodes


def main():
    input_file = "input.txt"
    caves = parse_input(input_file)
    # Cant figure out a way for backward generation with the small cave constraint
    paths = forward_generate_paths(caves)
    print(len(paths))


def forward_generate_paths(caves):
    completed_paths = []
    paths = []
    start_node = [cave for cave in caves if cave.name == "start"][0]
    end_node = [cave for cave in caves if cave.name == "end"][0]
    paths.append(Path(start_node))
    while paths:
        path = paths[0]
        current_node = path.get_last_node()
        neighbours = current_node.get_neighbours()
        for neighbour in neighbours:
            if not node_allowed(neighbour, path):
                continue

            path_copy = path.copy()
            path_copy.append(neighbour)
            if neighbour == end_node:
                completed_paths.append(path_copy)
            else:
                paths.append(path_copy)
        paths.remove(path)
    return completed_paths


def node_allowed(node, path):
    if node.is_small() and path.double_visited_small:
        return node not in path
    if node.name == "start":
        return False
    return True


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
