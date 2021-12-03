BIT_LENGTH = 12


def main():
    input_file = "input.txt"
    bit_statements = parse_statements(input_file)
    gammma_rate = get_string_of_most_common_bits(bit_statements)
    epsilon_rate = bit_flip(gammma_rate)
    print(int(gammma_rate, 2) * int(epsilon_rate, 2))


def parse_statements(input_file):
    binary_strings = []
    with open(input_file, encoding="ascii") as file:
        binary_strings = [line.strip() for line in file]
    return binary_strings


def bit_flip(binary_string):
    output = ""
    for i in binary_string:
        output += "0" if int(i) else "1"
    return output


def get_string_of_most_common_bits(statements):
    most_common_bits = ""
    statements_length = len(statements)
    chars_per_index = list(zip(*statements))
    for chars_at_index in chars_per_index:
        most_common_bits += str(
            int(chars_at_index.count("1") > (statements_length // 2))
        )
    return most_common_bits


if __name__ == "__main__":
    main()
