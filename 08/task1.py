def main():
    input_file = "input.txt"
    statements = parse_input(input_file)
    count = 0
    for statement in statements:
        for digit in statement[1]:
            if is_unique_length(digit):
                count += 1
    print(count)


def parse_input(input_file):
    statements = []
    with open(input_file) as file:
        for line in file:
            signal_patterns, four_digit_output = line.split(" | ")
            signal_patterns = signal_patterns.split()
            four_digit_output = four_digit_output.split()
            statements.append((signal_patterns, four_digit_output))
    return statements


def is_unique_length(digit_signal_pattern):
    length = len(digit_signal_pattern)
    return length in [2, 3, 4, 7]


if __name__ == "__main__":
    main()
