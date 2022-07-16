from dataclasses import dataclass


@dataclass
class Instruction:
    axis: str
    value: int


def main():
    paper_marks, instructions = parse_input_from_file("13/input.txt")
    for instruction in instructions:
        paper_marks = execute_instruction(paper_marks, instruction)

    print("task 2:")
    print(draw_paper(paper_marks))


def execute_instruction(paper_marks, instruction):
    if instruction.axis == "x":
        paper_marks = fold_left(paper_marks, instruction.value)
    else:
        paper_marks = fold_up(paper_marks, instruction.value)
    return paper_marks


def draw_paper(paper_marks):
    max_x = max(paper_marks, key=lambda x: x[0])[0]
    max_y = max(paper_marks, key=lambda x: x[1])[1]
    paper_line = ["."] * (max_x + 1)
    paper = [paper_line.copy() for _ in range(max_y + 1)]

    for mark in paper_marks:
        x, y = mark
        paper[y][x] = "#"

    return "\n".join(["".join(line) for line in paper])


def fold_left(paper_marks, value):
    updated_marks = []
    for mark in paper_marks:
        x, y = mark
        if x < value:
            updated_marks.append(mark)
        else:
            updated_marks.append((2 * value - x, y))
    return set(updated_marks)


def fold_up(paper_marks, value):
    updated_marks = []
    for mark in paper_marks:
        x, y = mark
        if y < value:
            updated_marks.append(mark)
        else:
            updated_marks.append((x, 2 * value - y))
    return set(updated_marks)


def parse_input_from_file(input_path):
    with open(input_path, encoding="ascii") as file:
        paper_marks_bare, instructions_bare = file.read().split("\n\n")
        paper_marks = [
            tuple(map(int, line.split(","))) for line in paper_marks_bare.splitlines()
        ]
        instructions = [
            parse_instruction(line) for line in instructions_bare.splitlines()
        ]
        return set(paper_marks), instructions


def parse_instruction(line):
    line_rest, value = line.split("=")
    return Instruction(line_rest[-1], int(value))


if __name__ == "__main__":
    main()
