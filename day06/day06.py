"""Day 06."""

from functools import reduce
import operator
from typing import Any, Iterator, TextIO

from utils.parse import read_lines

def solve_problem(nums, op_str):
    op = operator.add if op_str == "+" else operator.mul
    start = 0 if op == operator.add else 1
    return reduce(op, nums, start)


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 06."""
    lines = list(read_lines(file))
    nums = [line.split() for line in lines]
    num_cols = list(zip(*nums))
    letter_cols = list(zip(*lines))

    p1 = 0
    for num_col in num_cols:
        p1 += solve_problem([int(n) for n in num_col[:-1]], num_col[-1])

    p2 = 0
    nums = []
    for letter_col in reversed(letter_cols):
        joined = "".join(letter_col)
        if joined.strip() == "":
            continue
        nums.append(int(joined[:-1]))
        
        if letter_col[-1] != " ":
            p2 += solve_problem(nums, letter_col[-1])
            nums = []


    yield p1
    yield p2