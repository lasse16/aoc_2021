def main():
    group_size = 3
    input_file = "input.txt"
    statements = parse_input_into_statements(input_file)
    statement_differences = get_differences_between_consecutive_statement_groups(
        statements, group_size
    )
    print(len(list(filter(lambda x: x > 0, statement_differences))))


def get_differences_between_consecutive_statement_groups(statements, group_size):
    differences = []
    for index, statement in enumerate(statements[group_size:], group_size):
        differences.append(statement - statements[index - group_size])
    return differences


def parse_input_into_statements(input_file):
    statements = []
    with open(input_file, encoding="ascii") as file:
        statements = [int(line) for line in file]
    return statements


if __name__ == "__main__":
    main()
