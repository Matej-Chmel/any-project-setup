from pathlib import Path

def pathFromKey(d: dict, key: str, start: Path) -> Path:
	return (start / d.get(key, "")).resolve()
