from __future__ import annotations
from asyncio import create_task
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from src.common.CopyTask import CopyTask
from src.common.fileOps import ignoreStatus, parsePatterns, purgePatterns
from src.common.FileOpTask import FileOpTask
from src.common.MoveTask import MoveTask
from src.common.url import nameFromUrl
from src.common.zipFile import downloadZip, extractZip
from typing import ClassVar, Iterable

@dataclass
class Archive:
	root: ClassVar[Path]

	copyTasks: list[CopyTask]
	ignoredPatterns: list[str]
	moveTasks: list[MoveTask]
	purgePatterns: list[str]
	url: str

	@staticmethod
	def fromJSON(o: dict):
		return Archive(
			CopyTask.fromJSONArr(o.get("copy")),
			o.get("ignore"),
			MoveTask.fromJSONArr(o.get("move")),
			o.get("purge"),
			o["url"])

	@classmethod
	def fromJSONArr(cls, arr: list):
		return list(map(cls.fromJSON, arr))

	def ignoreStatus(self, p: Path):
		return ignoreStatus(p, self.ignored)

	def lateInit(self, dest: Path):
		self.url = self.url.rstrip("/")
		self.name = nameFromUrl(self.url)
		self.folder = dest / self.name

	def run(self, dest: Path):
		self.lateInit(dest)

		if Path(self.folder).exists():
			return f"{self.upperName()} already exists."

		with downloadZip(self.url) as z:
			extractZip(z, self.folder)

		self.ignored = parsePatterns(self.ignoredPatterns, self.folder)
		FileOpTask.runAll(self.moveTasks, self.startAtSlnLevel)
		FileOpTask.runAll(self.copyTasks, self.startAtSlnLevel)
		purgePatterns(self.purgePatterns, self.ignoreStatus, self.folder)
		return f"{self.upperName()} downloaded."

	@classmethod
	def runAll(self, entries: Iterable[Archive], dest: Path):
		f = partial(Archive.run, dest=dest)

		for e in entries:
			print(f(e))

	async def runAsync(self, dest: Path):
		return self.run(dest)

	def startAtSlnLevel(self, cond: bool):
		return Archive.root if cond else self.folder

	def task(self, dest: Path):
		return create_task(self.runAsync(dest))

	@classmethod
	def taskMap(cls, entries: Iterable[Archive], dest: Path):
		return map(partial(cls.task, dest=dest), entries)

	def upperName(self):
		return self.name.upper()
