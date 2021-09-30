from pathlib import Path
from src.common.platform import pythonCmd
from subprocess import call
from sys import version_info

def install(p: Path):
	call(map(str, [
		pythonCmd(), f"-{version_info.major}.{version_info.minor}",
		"-m", "pip", "install", "-r", p.resolve(), "--user"]))
