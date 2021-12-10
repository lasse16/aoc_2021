closing_char_value = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

opening_chunks = {
    "(",
    "[",
    "{",
    "<",
}

matching_chunks = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def main():
    input_file = "input.txt"
    lines = parse_input(input_file)
    completion_strings = {}
    for line in lines:
        comp_str = get_completion_string(line)
        if comp_str:
            completion_strings[line] = comp_str
    scores = sorted(
        [
            calculate_score_for_completion_string(comp_str)
            for comp_str in completion_strings.values()
        ]
    )
    print(f"middle score: {scores[len(scores) //2]}")


def calculate_score_for_completion_string(comp_str):
    score = 0
    for _char in comp_str:
        score = score * 5 + closing_char_value[_char]
    return score


def get_completion_string(line):
    stack = []
    for _char in line:
        if _char in opening_chunks:
            stack.append(_char)
        else:
            # closing char
            if len(stack) == 0:
                return None
            if stack.pop() != matching_chunks[_char]:
                # wrongly matched closing char
                return None
    if len(stack) == 0:
        return None
    return "".join([matching_chunks[opening_char] for opening_char in stack[::-1]])


def parse_input(input_file):
    with open(input_file) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    main()
