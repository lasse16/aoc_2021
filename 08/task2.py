from collections import Counter


def main():
    input_file = "input.txt"
    statements = parse_input(input_file)

    four_digit_values = [decode_four_digit(statement) for statement in statements]
    print(sum(four_digit_values))


def decode_four_digit(statement):
    signal_patterns, four_digit_output_value = statement
    mappings = [None] * 10
    mappings = get_easy_digits(signal_patterns, mappings)
    mappings = get_hard_digits(signal_patterns, mappings)
    mappings = [Counter(map) for map in mappings]
    output = int(
        "".join(
            [str(mappings.index(Counter(digit))) for digit in four_digit_output_value]
        )
    )
    return output


def get_easy_digits(signal_patterns, mappings):
    for pattern in signal_patterns:
        length = len(pattern)
        if length == 2:
            mappings[1] = pattern
        elif length == 3:
            mappings[7] = pattern
        elif length == 4:
            mappings[4] = pattern
        elif length == 7:
            mappings[8] = pattern
    return mappings


def get_hard_digits(signal_patterns, mappings):
    for pattern in signal_patterns:
        length = len(pattern)
        if length == 5:
            # 2,3,5
            if all([char_ in pattern for char_ in mappings[1]]):
                mappings[3] = pattern
            elif sum([char_ in pattern for char_ in mappings[4]]) == 3:
                mappings[5] = pattern
            else:
                mappings[2] = pattern
        elif length == 6:
            # 0,6,9
            if not all([char_ in pattern for char_ in mappings[1]]):
                mappings[6] = pattern
            elif not all([char_ in pattern for char_ in mappings[4]]):
                mappings[0] = pattern
            else:
                mappings[9] = pattern
    return mappings


def parse_input(input_file):
    statements = []
    with open(input_file) as file:
        for line in file:
            signal_patterns, four_digit_output = line.split(" | ")
            signal_patterns = signal_patterns.split()
            four_digit_output = four_digit_output.split()
            statements.append((signal_patterns, four_digit_output))
    return statements


if __name__ == "__main__":
    main()
