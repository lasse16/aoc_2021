from collections import Counter


def main():
    input_file = "input.txt"
    lantern_fish = parse_input(input_file)
    schools = Counter(lantern_fish)
    days = 256
    for _ in range(days):
        new_fish = schools[0]
        for i in range(8):
            schools[i] = schools[i + 1]
        schools[8] = new_fish
        schools[6] += new_fish
    print(f"lantern fish: {sum(schools.values())}")


def parse_input(input_file):
    with open(input_file, encoding="ascii") as file:
        return [int(x) for x in file.read().split(",")]


if __name__ == "__main__":
    main()
