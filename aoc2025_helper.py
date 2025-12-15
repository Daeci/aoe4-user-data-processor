from collections import deque
from enum import Enum, auto

# Day 4
class EdgeCase(Enum):
    NONE = auto()
    TOP_EDGE = auto()
    BOTTOM_EDGE = auto()
    LEFT_EDGE = auto()
    RIGHT_EDGE = auto()
    TOP_LEFT_CORNER = auto()
    TOP_RIGHT_CORNER = auto()
    BOTTOM_RIGHT_CORNER = auto()
    BOTTOM_LEFT_CORNER = auto()

class Positions(Enum):
    TOP = auto()
    TOP_RIGHT = auto()
    RIGHT = auto()
    BOTTOM_RIGHT = auto()
    BOTTOM = auto()
    BOTTOM_LEFT = auto()
    LEFT = auto()
    TOP_LEFT = auto()

class UniqueCoordsQueue:
    def __init__(self):
        self.queue = deque()
        self.seen = set()
    
    def enqueue(self, coord: tuple[int, int]) -> None:
        if coord not in self.seen:
            self.queue.append(coord)
            self.seen.add(coord)
    
    def dequeue(self) -> tuple[int, int]:
        if self.queue:
            coord = self.queue.popleft()
            self.seen.remove(coord)
            return coord
        return (-1, -1)
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def size(self) -> int:
        return len(self.queue)
    
    def contains(self, x: int, y: int) -> bool:
        return (x, y) in self.seen