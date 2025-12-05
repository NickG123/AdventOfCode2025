"""Day 05."""

from typing import Any, Iterator, TextIO

from utils.parse import read_sections


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 05."""
    range_strings, ingredients = read_sections(file)

    ranges = []    
    for r in range_strings:
        start, end = r.split("-")
        ranges.append(range(int(start), int(end) + 1))
        
    fresh_count = 0
    for ingredient in ingredients:
        number = int(ingredient)
        if any(number in r for r in ranges):
            fresh_count += 1

    sorted_ranges = sorted(ranges, key=lambda x: x.start)
    merged_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        last = merged_ranges[-1]
        if r.start <= last.stop - 1:
            merged_ranges[-1] = range(last.start, max(last.stop, r.stop))
        else:
            merged_ranges.append(r)


    yield fresh_count
    yield sum(r.stop - r.start for r in merged_ranges)