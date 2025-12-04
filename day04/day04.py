"""Day 04."""

from itertools import count
from typing import Any, Iterator, TextIO

from utils.geometry import DIRECTIONS, get_grid_point, iter_grid
from utils.parse import read_lines


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 04."""
    grid = [list(line) for line in read_lines(file)]
    accessable_rolls_p1 = 0
    accessable_rolls_p2 = 0

    for iteration in count():
        removed_points = []
        for val, p in iter_grid(grid):
            if val == "@":
                if sum((1 for dir in DIRECTIONS if get_grid_point(grid, p + dir) == "@")) < 4:
                    accessable_rolls_p2 += 1
                    if iteration == 0:
                        accessable_rolls_p1 += 1
                    removed_points.append(p)
        
        if not removed_points:
            break
        for p in removed_points:
            grid[p.y][p.x] = "."
            

    yield accessable_rolls_p1
    yield accessable_rolls_p2
