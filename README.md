# Setup for any project
Collection of Python scripts to setup project of any kind. Great for downloading libraries that are not part of the project.

## Guide

Add this repo as a submodule or clone it to the root directory of your project. Then run [build.py](build.py).

In the program, input what build script you want to use and path where the configuration for that script will be stored. The program will create a bash or batch file that will be used to run the build script.

Then create the configuration for your chosen build script.
- [Cleaner](#cleaner)
- [ZIP downloader](#zip-downloader)

## Cleaner
Cleans project of files specified in JSON file with configuration.

### Example configuration
```json
{
	"ignore": [
		"Debug/*.exe"
	],
	"purge": [
		"**/__pycache__",
		"Debug",
		"libs",
		"Release"
	],
	"root": ".."
}
```

### Keys
- `ignore`
	- Optional array of strings.
	- Ignore all paths in this array.
- `purge`
	- Optional array of strings.
	- Delete all paths in this array.
- `root`
	- Optional string.
	- Origin of all paths in the configuration.
	- The path of the configuration file is taken as an origin for this value.

## ZIP downloader
Downloads and extracts ZIP files. Great for libraries that are large and not all files from them are needed for your project. Don't forget to write a *.gitignore* if your project uses git so that the files this script downloads won't be committed.

### Example configuration
```json
{
	"archives": [
		{
			"copy": [
				{
					"from": "Debug/glew32.dll",
					"fromRoot": true,
					"to": "Release/"
				}
			],
			"ignore": [
				"lib/Win32"
			],
			"move": [
				{
					"from": "bin/Release/Win32/glew32.dll",
					"to": "Debug/"
				}
			],
			"purge": [
				"bin",
				"doc",
				"lib",
				"Makefile.txt"
			],
			"url": "https://github.com/nigels-com/glew/releases/download/glew-2.2.0/glew-2.2.0-win32.zip"
		}
	],
	"dest": "libs",
	"root": ".."
}
```

### Keys
- `archives`
	- Required array of objects.
	- Archives to be downloaded and extracted.
	- Objects also contain information about file operations that will be carried out after the archive has been extracted.
	- Object keys:
		- `copy`
			- Optional array of objects.
			- What files to copy and where.
			- Object keys:
				- `from`
					- Required string.
					- Path to a file or folder being copied.
					- Origin of this path is root folder of the extracted archive if not specified otherwise by `fromRoot` key.
				- `fromRoot`
					- Optional boolean.
					- Default value is `false`.
					- If `true`, origin of the path in `from` is in `root` key.
				- `to`
					- Required string.
					- Path of the new copy.
					- Origin of this path is in `root` key.
					- If this path ends with `/`, name of the copied file is appended to this path.
				- `toRoot`
					- Optional boolean.
					- Default value is `true`.
					- If `false`, origin of the path in `to` is root folder of the extracted archive.
		- `ignore`
			- Optional array of strings.
			- Ignore all paths in this array.
		- `move`
			- Optional array of objects.
			- Same as `copy`.
			- What files to move and where.
		- `purge`
			- Optional array of strings.
			- Delete all paths in this array.
		- `url`
			- Required string.
			- URL of the archive.
- `dest`
	- Optional string.
	- Path to folder where all archives will be extracted.
	- Origin of this path is in `root` key.
	- If absent, archives will be extracted to folder in `root`.
- `root`
	- Optional string.
	- Origin of all paths in the configuration if not specified otherwise.
	- The path of the configuration file is taken as an origin for this value.
