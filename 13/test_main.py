from task1 import parse_input_from_file, fold_up, Instruction


def test_input_parsing():
    paper_marks, instructions = parse_input_from_file("13/test_input.txt")
    assert instructions == expected_instructions
    assert expected_paper_marks == paper_marks


def test_example_fold():
    paper_marks = fold_up(expected_paper_marks, 7)
    assert len(paper_marks) == 17


expected_paper_marks = [
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
]
expected_instructions = [Instruction("y", 7), Instruction("x", 5)]
