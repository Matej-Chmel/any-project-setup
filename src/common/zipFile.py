from io import BytesIO
from pathlib import Path
from src.common.AppError import AppError
from zipfile import ZipFile

def downloadZip(url: str):
	from requests import get

	with get(url) as r:
		if not r.ok:
			raise AppError(f"Failed to download {url}.")
		return ZipFile(BytesIO(r.content))

def extractZip(z: ZipFile, destRoot: Path):
	z.extractall(destRoot.parent)
	rootName = rootNameOfZip(z)

	if destRoot.name != rootName:
		(destRoot.parent / rootName).rename(destRoot)

def rootNameOfZip(z: ZipFile):
	return Path(z.namelist()[0]).name
