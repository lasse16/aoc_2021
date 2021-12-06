def main():
    input_file = "input.txt"
    lantern_fish = parse_input(input_file)
    days = 80
    for _ in range(days):
        new_fish = lantern_fish.count(0)
        updated_fishes = [-1] * len(lantern_fish)
        for index, fish in enumerate(lantern_fish):
            updated_fishes[index] = (fish - 1) if fish > 0 else 6
        updated_fishes.extend([8 for _ in range(new_fish)])
        lantern_fish = updated_fishes
    print(f"lantern fish: {len(lantern_fish)}")


def parse_input(input_file):
    with open(input_file, encoding="ascii") as file:
        return [int(x) for x in file.read().split(",")]


if __name__ == "__main__":
    main()
