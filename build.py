from pathlib import Path
from platform import system

class AppError(Exception):
	pass

def confirm(prompt: str):
	return input(prompt).strip().lower() in ["y", "yes"]

def formatSource(s: str, module: str, cfg: Path):
	return s.replace("{MODULE}", module, 1).replace("{CFG}", str(cfg), 1)

def inputAll(projectRoot: Path, template: Path):
	return inputModule(), inputCfgPath(projectRoot), inputRunnerPath(projectRoot, template)

def inputCfgPath(origin: Path):
	p = Path(input(
		"Enter path to JSON file with configuration.\n"
		"It doesn't need to exist now. You can create it later.\n"
		"The path's origin is at your project root directory.\n"
		"Example: cfg/libs.json\n"))

	if p.suffix != ".json" and not confirm("The file's extension is not .json. Continue anyway? (y/n) "):
		raise AppError("Aborted.")
	return (origin / p).resolve().relative_to(origin)

def inputModule():
	modules = {
		1: "cleaner",
		2: "zipDownloader"}
	modulesStr = "\n".join(f"{k}: {v.capitalize()}" for k, v in modules.items())

	try:
		return modules[int(input(f"Select build script by number:{NL}{modulesStr}{NL}"))]
	except KeyError as e:
		raise AppError(f"Invalid module number: {e.args[0]}")
	except ValueError:
		raise AppError("Not a number.")

def inputRunnerPath(projectRoot: Path, template: Path):
	p = projectRoot / input("Enter name for the generated script: ")

	if p.suffix != template.suffix:
		return p.with_suffix(template.suffix)
	return p

def main():
	projectRoot, templatesDir = paths()
	template = templateScript(templatesDir)

	try:
		module, cfg, runner = inputAll(projectRoot, template)
	except AppError as e:
		return print(e)

	with openPath(template) as f:
		source = formatSource(f.read(), module, cfg)

	with openPath(runner, "w") as f:
		f.write(source)
	print(f"Generated {runner}")
	input("Press ENTER to exit.")

NL = "\n"

def openPath(p: Path, mode="r"):
	return p.open(mode, encoding="utf-8")

def onWindows():
	return system().lower().startswith("windows")

def paths():
	scriptDir = Path(__file__).absolute().parent
	return scriptDir.parent, scriptDir / "templates"

def templateScript(d: Path):
	return d / f"template.{'bat' if onWindows() else 'sh'}"

if __name__ == "__main__":
	main()
