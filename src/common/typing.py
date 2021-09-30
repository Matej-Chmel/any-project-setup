from pathlib import Path
from typing import Any, Callable, Coroutine, Iterable, Union

AnyToAny = Callable[[Any], Any]
BoolToPath = Callable[[bool], Path]
IterableOrNone = Union[Iterable, None]
VoidToCoroutine = Callable[[], Coroutine[Any, Any, None]]
VoidToNone = Callable[[], None]
