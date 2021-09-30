from itertools import chain
from pathlib import Path
from shutil import rmtree
from src.common.IgnoreStatus import IgnoreStatus, PathToIgnoreStatus
from src.common.itertools import safeIter
from typing import Union

def checkAndPurge(p: Path, ignoreStatus: PathToIgnoreStatus):
	if (status := ignoreStatus(p)) == IgnoreStatus.NOT_IGNORED:
		purge(p)
	elif status == IgnoreStatus.SOME_CHILDREN_IGNORED:
		for child in p.iterdir():
			checkAndPurge(child, ignoreStatus)

def ignoreStatus(p: Path, ignored: Union[list[Path], None]):
	for i in safeIter(ignored):
		if p.is_relative_to(i):
			return IgnoreStatus.IGNORED
		if i.is_relative_to(p):
			return IgnoreStatus.SOME_CHILDREN_IGNORED
	return IgnoreStatus.NOT_IGNORED

def parsePatterns(patterns: Union[list[str], None], start: Path):
	return list(chain.from_iterable(start.glob(p) for p in safeIter(patterns)))

def purge(p: Path):
	if p.is_dir():
		rmtree(p)
	else:
		p.unlink()

def purgePatterns(patterns: Union[list[str], None], ignoreStatus: PathToIgnoreStatus, start: Path):
	for p in parsePatterns(patterns, start):
		checkAndPurge(p, ignoreStatus)
