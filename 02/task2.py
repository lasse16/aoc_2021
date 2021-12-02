def main():
    input_file = "input.txt"
    instructions = parse_input_into_statements(input_file)
    starting_position = (0, 0, 0)
    x_pos, y_pos = execute_instructions(instructions, starting_position)
    print(x_pos * y_pos)


def execute_instructions(instructions, starting_position):
    forward_sum = starting_position[0]
    depth = starting_position[1]
    aim = starting_position[2]

    for instruction in instructions:
        instruction_type = instruction[0]
        instruction_value = instruction[1]
        if instruction_type == "forward":
            forward_sum += instruction_value
            depth += aim * instruction_value
        elif instruction_type == "down":
            aim += instruction_value
        elif instruction_type == "up":
            aim -= instruction_value

    return forward_sum, depth


def parse_input_into_statements(input_file):
    statements = []
    with open(input_file, "r", encoding="ascii") as file:
        for line in file:
            instruction, value = tuple(line.split(" "))
            statements.append((instruction, int(value)))
    return statements


if __name__ == "__main__":
    main()
