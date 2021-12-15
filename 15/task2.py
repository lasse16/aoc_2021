import math
import heapq


def main():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    cave_risk = parse_input(input_file)
    cave_risk = expand_map(cave_risk)
    shortest_path_weight = djikstra(cave_risk, (0, 0))
    print(shortest_path_weight[(len(cave_risk[0]) - 1, len(cave_risk) - 1)])


def expand_map(tile):
    X, Y = len(tile), len(tile[0])
    return [
        [(tile[x % X][y % Y] + x // X + y // Y - 1) % 9 + 1 for y in range(5 * Y)]
        for x in range(5 * X)
    ]


def djikstra(weights, start_node):
    costs = {start_node: 0}
    predecessor = {}
    visited = set()
    heapq.heappush(Q := [], (0, start_node))

    while Q:
        current_node = heapq.heappop(Q)[1]
        visited.add(current_node)
        current_weight = costs[current_node]
        for neighbour in get_neighbours(current_node):
            if neighbour in visited:
                continue
            neighbour_weight = current_weight + weights[neighbour[0]][neighbour[1]]
            if neighbour_weight < costs.get(neighbour, math.inf):
                costs[neighbour] = neighbour_weight
                predecessor[neighbour] = current_node
                heapq.heappush(Q, (neighbour_weight, neighbour))
    return costs


def get_neighbours(current_node_index):
    max_x = 500
    max_y = 500
    neighbours = [
        tuple(map(lambda x, y: x + y, current_node_index, shift))
        for shift in ((0, 1), (1, 0), (0, -1), (-1, 0))
    ]
    return [
        neighbour
        for neighbour in neighbours
        if neighbour[0] in range(max_x) and neighbour[1] in range(max_y)
    ]


def parse_input(input_file):
    risk_tiles = []
    with open(input_file) as file:
        risk_tiles = [[int(x) for x in line.strip()] for line in file]

    return risk_tiles


if __name__ == "__main__":
    main()
