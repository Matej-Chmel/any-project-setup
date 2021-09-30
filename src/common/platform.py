from platform import system

def onWindows():
	return system().lower().startswith('windows')

def pythonCmd():
	return "py" if onWindows() else "python"
