class Board:
    def __init__(self, lines) -> None:
        self.rows = [[int(number) for number in line.split()] for line in lines]
        columns = [[] for _ in self.rows[0]]
        for row in self.rows:
            for col_index, element in enumerate(row):
                columns[col_index].append(element)
        self.columns = columns

    def mark_number_on_board(self, number):
        for line in self.rows:
            for index_, number_on_board in enumerate(line):
                if number_on_board == number:
                    line[index_] = -1
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


def main():
    input_file = "input.txt"
    called_numbers, boards = parse_input(input_file)
    for number in called_numbers:
        for board in boards:
            board.mark_number_on_board(number)
            if board.is_won():
                sum_ = board.sum_unchecked_numbers()
                print(f"winning_board score: { sum_ * number}")
                return

    print("No solution found")


def parse_input(input_file):
    with open(input_file) as file:
        paragraphs = file.read().split("\n\n")
        called_numbers = [int(x) for x in paragraphs[0].split(",")]
        boards = [Board(paragraph.splitlines()) for paragraph in paragraphs[1:]]
        return called_numbers, boards


if __name__ == "__main__":
    main()
