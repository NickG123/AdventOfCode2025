"""Day 07."""

from typing import Any, Counter, Iterator, TextIO

from utils.parse import read_lines


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 07."""
    lines = read_lines(file)
    first_line = next(lines)
    
    beams = Counter([first_line.index("S")]) 
    split_count = 0

    for line in lines:
        for beam, count in list(beams.items()):
            if line[beam] == "^":
                split_count += 1
                del beams[beam]
                beams[beam - 1] += count
                beams[beam + 1] += count
            

    yield split_count
    yield sum(beams.values())
