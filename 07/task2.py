import math


def main():
    input_file = "input.txt"
    crab_submarines = parse_input(input_file)
    print(geometric_median(crab_submarines))


def geometric_median(points):
    max_ = max(points)
    min_ = min(points)
    minimal_cost = math.inf
    minimal_cost_guess = -1
    for i in range(min_, max_ + 1):
        cost = get_distance_for_guess(i, points)
        if cost < minimal_cost:
            minimal_cost = cost
            minimal_cost_guess = i

    print(minimal_cost)
    return minimal_cost_guess


def get_distance_for_guess(guess, points):
    cost = 0
    for point in points:
        cost += sum_until(abs(point - guess))
    return cost


def sum_until(integer):
    return (integer * (integer + 1)) // 2


def parse_input(input_file):
    with open(input_file, encoding="ascii") as file:
        return [int(x) for x in file.read().split(",")]


if __name__ == "__main__":
    main()
