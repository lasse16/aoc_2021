from collections import Counter
from typing import List
import re

start_char = ""
end_char = ""


class Rule:
    starting_pair: str
    resulting_pairs: List[str]

    def __init__(self, starting_pair, resulting_pairs):
        self.starting_pair = starting_pair
        self.resulting_pairs = resulting_pairs


def main():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    start_polymer, rules = parse_input(input_file)
    steps = 40
    polymer = start_polymer
    for _ in range(steps):
        polymer = do_step(polymer, rules)
    polymer_counter = create_polymer_counter(polymer)
    counts = polymer_counter.most_common()
    print(counts[0][1] - counts[-1][1])


def create_polymer_counter(polymer):
    total = Counter()
    for pair, count in polymer.items():
        for char_ in pair:
            total[char_] += count
    total[start_char] += 1
    total[end_char] += 1
    for char_, count in total.items():
        total[char_] = count // 2
    return total


def do_step(polymer, rules):
    new_polymer = {}
    for pair, count in polymer.items():
        for result in rules[pair].resulting_pairs:
            new_polymer[result] = new_polymer.get(result, 0) + count
    return new_polymer


def parse_input(input_file):
    global start_char, end_char
    rules = {}
    polymer = {}
    rule_pattern = re.compile(r"([A-Z]{2}) -> ([A-Z])")
    with open(input_file) as file:
        starting_polymer, rules_bare = file.read().split("\n\n")
        start_char = starting_polymer[0]
        end_char = starting_polymer[-1]
        pairs_in_polymer = [
            "".join(pair) for pair in zip(starting_polymer, starting_polymer[1:])
        ]
        for pair in pairs_in_polymer:
            polymer[pair] = polymer.get(pair, 0) + 1

        for rule in rules_bare.splitlines():
            starting_pair, inserted_char = rule_pattern.match(rule).groups()
            resulting_pairs = []
            resulting_pairs.append(starting_pair[0] + inserted_char)
            resulting_pairs.append(inserted_char + starting_pair[1])
            rules[starting_pair] = Rule(starting_pair, resulting_pairs)
    return polymer, rules


if __name__ == "__main__":
    main()
