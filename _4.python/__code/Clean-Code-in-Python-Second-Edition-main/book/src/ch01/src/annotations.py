"""Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

> Annotations
"""
from dataclasses import dataclass
from typing import Tuple

Client = Tuple[int, str]


def process_clients(clients: list[Client]):  # type: ignore
    ...


@dataclass
class Point:
    lat: float
    long: float


def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""
    return Point(latitude, longitude)
