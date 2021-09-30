from __future__ import annotations
from dataclasses import dataclass
from src.common.itertools import listOrNone, mapOrNone, safeIter
from src.common.typing import BoolToPath
from typing import Iterable, Union

@dataclass
class FileOpTask:
	fromRoot: bool
	fromStr: str
	toRoot: bool
	toStr: str

	def carryOut(self):
		raise NotImplementedError

	@classmethod
	def fromJSON(cls, o: dict):
		return cls(o.get("fromRoot", False), o["from"], o.get("toRoot", True), o["to"])

	@classmethod
	def fromJSONArr(cls, arr: list):
		return listOrNone(mapOrNone(cls.fromJSON, arr))

	def lateInit(self, startDecider: BoolToPath):
		self.fromPath = startDecider(self.fromRoot) / self.fromStr
		self.toPath = startDecider(self.toRoot) / self.toStr

		if self.toStr.endswith("/"):
			self.toPath = self.toPath / self.fromPath.name

	def run(self, startDecider: BoolToPath):
		self.lateInit(startDecider)
		self.toPath.parent.mkdir(exist_ok=True, parents=True)
		self.carryOut()

	@classmethod
	def runAll(cls, tasks: Union[Iterable[FileOpTask], None], startDecider: BoolToPath):
		for t in safeIter(tasks):
			t.run(startDecider)
