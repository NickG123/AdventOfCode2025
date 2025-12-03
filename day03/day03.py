"""Day 03."""

from typing import Any, Iterator, TextIO
from utils.parse import read_lines

def find_joltage(vals: list[int], depth: int) -> int:
    """Find the maximum joltage difference."""
    if depth == 0:
        return 0
    max_val = None
    max_pos = None
    for i, val in enumerate(vals[:-depth + 1] if depth > 1 else vals):
        if max_val is None or val > max_val:
            max_val = val
            max_pos = i
    return max_val * (10 ** (depth - 1)) + find_joltage(vals[max_pos + 1 :], depth - 1)
    

def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 03."""
    p1_joltage = 0
    p2_joltage = 0
    for line in read_lines(file):
        vals = [int(char) for char in line]
        p1_joltage += find_joltage(vals, 2)
        p2_joltage += find_joltage(vals, 12)
    yield p1_joltage
    yield p2_joltage