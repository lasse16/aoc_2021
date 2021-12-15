import math
import heapq

max_x = 100
max_y = 100


def main():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    cave_risk = parse_input(input_file)
    shortest_path_weight = djikstra(cave_risk, (0, 0))
    print(shortest_path_weight[(max_x - 1, max_y - 1)])


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
