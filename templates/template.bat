@echo off

rem Move to directory of any-project-setup.
set scriptDir=%~dp0
set scriptDir=%scriptDir:~0, -1%
cd %scriptDir%\any-project-setup

py -m src.{MODULE}.main %scriptDir%\{CFG}
