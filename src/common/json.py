from json import load
from pathlib import Path

def dictFromJSON(p: Path) -> dict:
	return JSON(p)

def JSON(p: Path):
	with Path(p).open("r", encoding="utf-8") as f:
		return load(f)

def listFromJSON(p: Path) -> list:
	return JSON(p)
