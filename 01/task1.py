def main():
    input_file = "input.txt"
    statements = parse_input_into_statements(input_file)
    statement_differences = get_differences_between_consecutive_statements(statements)
    print(len(list(filter(lambda x: x > 0, statement_differences))))


def get_differences_between_consecutive_statements(statements):
    previous_statement = statements[0]
    differences = []
    for statement in statements:
        differences.append(statement - previous_statement)
        previous_statement = statement
    return differences


def parse_input_into_statements(input_file):
    statements = []
    with open(input_file, encoding="ascii") as file:
        statements = [int(line) for line in file]
    return statements


if __name__ == "__main__":
    main()
