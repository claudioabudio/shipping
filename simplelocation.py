from dataclasses import dataclass
from position import Position


@dataclass(eq=True, frozen=True)
class SimpleLocation:
    name: str
    position: Position

