"""Day 08."""
from __future__ import annotations

from functools import reduce
from itertools import islice
import operator
from typing import Any, Iterator, TextIO
from dataclasses import dataclass

from utils.parse import read_number_list

@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def distance(self, other: Point3D) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

def find_distances(points: list[Point3D]) -> list[tuple[float, Point3D, Point3D]]:
    """I'm sure there's a better way than finding every possible distacne..."""
    results = []
    for i, start in enumerate(points):
        for end in points[i + 1:]:
            dist = start.distance(end)
            results.append((dist, start, end))
    return results

def merge_clusters(clusters: list[set[Point3D]], p1: Point3D, p2: Point3D) -> None:
    """Merge clusters containing p1 and p2."""
    cluster1 = None
    cluster2 = None
    for cluster in clusters:
        if p1 in cluster:
            cluster1 = cluster
        if p2 in cluster:
            cluster2 = cluster
    if cluster1 is not None and cluster2 is not None and cluster1 != cluster2:
        cluster1.update(cluster2)
        clusters.remove(cluster2)
    elif cluster1 is not None:
        cluster1.add(p2)
    elif cluster2 is not None:
        cluster2.add(p1)
    else:
        clusters.append({p1, p2})

def run(file: TextIO) -> Iterator[Any]:
    """Solution for Day 08."""
    points = [Point3D(*nums) for nums in read_number_list(file, sep=",")]
    distances = find_distances(points)
    distances.sort(key=lambda x: x[0])

    clusters = []


    for i, (_, p1, p2) in enumerate(distances):
        merge_clusters(clusters, p1, p2)
        if i == 1000:
            yield reduce(operator.mul, islice(sorted([len(c) for c in clusters], reverse=True), 0, 3), 1)
        if len(clusters) == 1 and len(clusters[0]) == len(points):
            yield p1.x * p2.x
            break
    

            
        