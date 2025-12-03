"""Day 02."""

from itertools import count
from typing import Any, Iterator, TextIO


def find_invalid_ids(min_id: str, max_id: str, repeat_count: int) -> Iterator[int]:
    """Find invalid IDs within a range."""
    full_length, fractional_length = divmod(len(min_id), repeat_count)
    if fractional_length == 0:
        start_seg = int(min_id[:full_length])
    else:
        start_seg =  (10 ** (len(min_id) // repeat_count))
    for seg in count(start_seg):
        full_id = int(str(seg) * repeat_count)
        if full_id > int(max_id):
            return
        if full_id >= int(min_id):
            yield full_id


def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 02."""
    p1_sum = 0
    p2_sum = 0
    for r in next(file).split(","):
        minimum, maximum = r.split("-")
        invalid_ids = set()
        for repeat in range(2, len(maximum) + 1):
            for invalid_id in find_invalid_ids(minimum, maximum, repeat):
                invalid_ids.add(invalid_id)
                if repeat == 2:
                    p1_sum += int(invalid_id)
        p2_sum += sum(invalid_ids)


    yield p1_sum
    yield p2_sum