from enum import auto, Enum
from pathlib import Path
from typing import Callable

class IgnoreStatus(Enum):
	IGNORED = auto()
	NOT_IGNORED = auto()
	SOME_CHILDREN_IGNORED = auto()

PathToIgnoreStatus = Callable[[Path], IgnoreStatus]
