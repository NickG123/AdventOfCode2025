"""Day 01."""

from typing import Any, Iterator, TextIO


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 01."""
    dial = 50
    zero_count = 0
    zero_pass_count = 0

    for line in file:
        match (line[0], int(line[1:])):
            case "L", rot:
                new_dial = (dial - rot) % 100
                if (new_dial > dial and dial != 0) or new_dial == 0:
                    zero_pass_count += 1
            case "R", rot:
                new_dial = (dial + rot) % 100
                if new_dial < dial:
                    zero_pass_count += 1
            case _:
                raise ValueError(f"Invalid input line: {line}")
            
        dial = new_dial
        zero_pass_count += (rot // 100)

        if dial == 0:
            zero_count += 1
               
    yield zero_count
    yield zero_pass_count
