from typing import Tuple, List
import sys

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}
id_totals = 0

if len(sys.argv) < 1:
    print("This program requires a filepath to the input.")
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()


def parse_game(game_line: str) -> Tuple[str, List[list]]:
    game_line = game_line.strip("\n")
    game_id = game_line.split()[1].strip(":")
    sets = [i.split(", ") for i in game_line.split(": ")[1].split("; ")]
    return game_id, sets


def parse_set(_set: List[str]) -> List[Tuple[str, int]]:
    return [(int(c.split()[0]), c.split()[1]) for c in _set]


def is_possible(highest_numbers: dict[str, int]):
    for color, highest_count in highest_numbers.items():
        if LIMITS.get(color) < highest_count:
            return False
    return True


for line in lines:
    game_id, sets = parse_game(line)
    highs = {}
    for i in sets:
        for color_count, color_name in parse_set(i):
            if highs.get(color_name, 0) < color_count:
                highs[color_name] = color_count
    if is_possible(highs):
        id_totals += int(game_id)
print(id_totals)