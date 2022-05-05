import sys
import re


def main():
    paper, instructions = parse_input("test_input.txt")
    print(paper.to_string())


def parse_input(file_path):
    with open(file_path) as file:
        text = file.read()
        split_text = text.split("\n\n")
        paper_dots_bare = split_text[0]
        instructions_bare = split_text[1]
        dots = [tuple(map(int, x.split(","))) for x in paper_dots_bare.splitlines()]
        paper = Paper(dots)
        reg_ex = re.compile("fold along (x|y)=(\d+)")
        instructions = [
            Instruction(*reg_ex.match(instruction).groups())
            for instruction in instructions_bare.splitlines()
        ]
        return paper, instructions


class Paper(object):
    def __init__(self, dots):
        self.max_x = max(dots, key=lambda x: x[0])[0]
        self.max_y = max(dots, key=lambda x: x[1])[1]

        self.dots = dots

    def to_string(self):
        # def __repr__(self):
        blank_paper = [
            ["." for _ in range(self.max_x + 1)] for _ in range(self.max_y + 1)
        ]
        for dot in self.dots:
            x, y = dot
            blank_paper[y][x] = "#"
        return "\n".join(["".join(x) for x in blank_paper])


class Instruction(object):
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value

    def __repr__(self):
        axis, value = (self.axis, self.value)
        return f"fold along {axis}={value}"


if __name__ == "__main__":
    main()
