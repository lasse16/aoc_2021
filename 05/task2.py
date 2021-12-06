from dataclasses import dataclass
import re
from collections import Counter


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return self.x ** 2 * self.y

    def __repr__(self):
        return f"({self.x},{self.y})"


@dataclass
class Line:
    start: Point
    end: Point

    def horizontal(self):
        return self.start.x == self.end.x

    def vertical(self):
        return self.start.y == self.end.y

    def points_on_line(self):
        points = set()
        direction = get_direction_from_start_end(self.start, self.end)
        current_point = self.start
        while current_point != self.end:
            points.add(current_point)
            current_point = Point(
                current_point.x + direction[0], current_point.y + direction[1]
            )

        points.add(self.end)
        return points

    def __repr__(self):
        return f"({self.start}->{self.end})"


def get_direction_from_start_end(a, b):
    def sign(x):
        if x > 0:
            return 1
        if x == 0:
            return 0
        return -1

    return sign(b.x - a.x), sign(b.y - a.y)


def main():
    input_file = "input.txt"
    vent_lines = parse_input(input_file)
    points = Counter(
        [
            point
            for line in [list(line.points_on_line()) for line in vent_lines]
            for point in line
        ]
    )
    print(len(list(filter(lambda x: x[1] > 1, points.items()))))


def parse_input(input_file):
    lines = []
    regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    with open(input_file, encoding="ascii") as file:
        for line in file:
            matched = regex.match(line)
            groups = [int(x) for x in matched.groups()]
            lines.append(Line(Point(groups[0], groups[1]), Point(groups[2], groups[3])))
    return lines


if __name__ == "__main__":
    main()
