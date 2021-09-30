from functools import partial
from pathlib import Path
from src.common.asyncio import runAsyncOrSync, runCoros
from src.common.Cfg import Cfg
from src.common.install import install
from src.common.pathlib import pathFromKey
from src.zipDownloader.Archive import Archive

def commonMain():
	cfg = Cfg.fromArgs("ZIP_DOWNLOADER", "Downloads and extracts ZIP files, e.g. libraries.")
	dest = pathFromKey(cfg, "dest", cfg.root)
	dest.mkdir(exist_ok=True)
	Archive.root = cfg.root
	install(Path(__file__).with_name("requirements.txt"))
	return dest, Archive.fromJSONArr(cfg["archives"])

def main(dest: Path, items: list[Archive]):
	Archive.runAll(items, dest)

async def mainAsync(dest: Path, items: list[Archive]):
	await runCoros(Archive.taskMap(items, dest))

if __name__ == "__main__":
	dest, items = commonMain()
	runAsyncOrSync(False, partial(mainAsync, dest, items), partial(main, dest, items))
