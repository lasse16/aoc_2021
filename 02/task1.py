def main():
    input_file = "input.txt"
    instructions = parse_input_into_statements(input_file)
    starting_position = (0, 0)
    x_pos, y_pos = execute_instructions(instructions, starting_position)
    print(x_pos * y_pos)


def execute_instructions(instructions, starting_position):
    forward_sum = starting_position[0]
    downward_sum = starting_position[1]
    upward_sum = starting_position[1]

    for instruction in instructions:
        instruction_type = instruction[0]
        instruction_value = instruction[1]
        if instruction_type == "forward":
            forward_sum += instruction_value
        elif instruction_type == "down":
            downward_sum += instruction_value
        elif instruction_type == "up":
            upward_sum += instruction_value

    return forward_sum, downward_sum - upward_sum


def parse_input_into_statements(input_file):
    statements = []
    with open(input_file, "r", encoding="ascii") as file:
        for line in file:
            instruction, value = tuple(line.split(" "))
            statements.append((instruction, int(value)))
    return statements


if __name__ == "__main__":
    main()
