corrupted_bracket_score = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

closing_chunks = {
    ")",
    "]",
    "}",
    ">",
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
    score = 0
    for line in lines:
        score += corrupted_bracket_score[corrupted(line)]
    print(f"score: {score}")


def corrupted(line):
    stack = []
    for _char in line:
        if _char in opening_chunks:
            stack.append(_char)
        else:
            # closing char
            if len(stack) == 0:
                return _char
            if stack.pop() != matching_chunks[_char]:
                # wrongly matched closing char
                return _char
    return ""


# def incomplete(line):
#     stack = []
#     for _char in line[::-1]:
#         if _char in closing_chunks:
#             stack.append(_char)
#         else:
#             if len(stack) == 0:
#                 # unmatched opening
#                 return True
#             if stack.pop() != matching_chunks[_char]:
#                 # line is corrupted
#                 return False
#     return False


def parse_input(input_file):
    with open(input_file) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    main()
