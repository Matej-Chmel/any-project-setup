from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from src.common.json import dictFromJSON
from src.common.pathlib import pathFromKey

@dataclass
class Cfg:
	json: dict
	path: Path

	def __getitem__(self, key):
		return self.json[key]

	def __post_init__(self):
		self.root = pathFromKey(self.json, "root", self.path.parent)

	@classmethod
	def fromArgs(cls, progName: str, desc: str):
		parser = ArgumentParser(prog=progName, description=desc)
		parser.add_argument("cfg", help="Path to JSON file with configuration.")
		path = Path(parser.parse_args().cfg)
		return cls(dictFromJSON(path), path)

	def get(self, key, default=None):
		return self.json.get(key, default)
