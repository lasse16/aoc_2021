class Board:
    def __init__(self, lines, id) -> None:
        self.rows = [[int(number) for number in line.split()] for line in lines]
        columns = [[] for _ in self.rows[0]]
        for row in self.rows:
            for col_index, element in enumerate(row):
                columns[col_index].append(element)
        self.columns = columns
        self.id = id

    def mark_number_on_board(self, number):
        for row_index, line in enumerate(self.rows):
            for col_index, number_on_board in enumerate(line):
                if number_on_board == number:
                    line[col_index] = -1
                    self.columns[col_index][row_index] = -1
                    return

    def is_won(self):
        winning_row = [-1 for _ in self.rows]
        return winning_row in self.columns or winning_row in self.rows

    def sum_unchecked_numbers(self) -> int:
        total = 0
        for row in self.rows:
            for element in row:
                if element >= 0:
                    total += element
        return total

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Board) and o.id == self.id

    def __hash__(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return str(self.id)


def main():
    input_file = "input.txt"
    called_numbers, boards = parse_input(input_file)
    won_boards = []
    final_number = 0
    for number in called_numbers:
        remaining_boards = [board for board in boards if board not in won_boards]
        if not remaining_boards:
            break
        for board in remaining_boards:
            board.mark_number_on_board(number)
            if board.is_won():
                won_boards.append(board)
        final_number = number

    print(
        f"last board to win score: {final_number * won_boards[-1].sum_unchecked_numbers()}"
    )


def parse_input(input_file):
    with open(input_file) as file:
        paragraphs = file.read().split("\n\n")
        called_numbers = [int(x) for x in paragraphs[0].split(",")]
        boards = [
            Board(paragraph.splitlines(), i)
            for i, paragraph in enumerate(paragraphs[1:])
        ]
        return called_numbers, boards


if __name__ == "__main__":
    main()
