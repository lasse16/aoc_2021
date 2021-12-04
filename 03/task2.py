BIT_LENGTH = 12


def main():
    input_file = "input.txt"
    bit_statements = parse_statements(input_file)
    oxygen = search_by_function(bit_statements, lambda x: x)
    # flip one single bit: ~x + 2
    co2 = search_by_function(bit_statements, lambda x: ~x + 2)
    print(int(oxygen, 2) * int(co2, 2))


def parse_statements(input_file):
    binary_strings = []
    with open(input_file, encoding="ascii") as file:
        binary_strings = [line.strip() for line in file]
    return binary_strings


def search_by_function(statements, filter_function):
    current_statements = statements
    current_bit_index = 0
    while len(current_statements) > 1:
        print(f"{current_bit_index} bit index")
        statements_sorted_by_current_bit = {1: [], 0: []}
        current_most_common_bit = 0
        for statement in current_statements:
            bit = int(statement[current_bit_index])
            statements_sorted_by_current_bit[bit].append(statement)
            # Makes 0 -> -1 and 1->1
            current_most_common_bit += (bit * 2) - 1
        current_most_common_bit = 0 if current_most_common_bit < 0 else 1
        current_statements = statements_sorted_by_current_bit[
            filter_function(current_most_common_bit)
        ]
        current_bit_index += 1

    final_statement = current_statements[0]
    return final_statement


if __name__ == "__main__":
    main()
