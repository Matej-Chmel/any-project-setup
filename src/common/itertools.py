from functools import lru_cache
from src.common.typing import AnyToAny, IterableOrNone

def listOrNone(i: IterableOrNone):
	return None if i is None else list(i)

def mapOrNone(f: AnyToAny, i: IterableOrNone):
	return None if i is None else map(f, i)

class NoneIterator:
	def __iter__(self):
		return self

	def __next__(self):
		raise StopIteration

@lru_cache(1)
def NoneIteratorInstance():
	return NoneIterator()

def safeIter(i: IterableOrNone):
	return NoneIteratorInstance() if i is None else i
