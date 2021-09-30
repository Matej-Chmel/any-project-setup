from shutil import copy
from src.common.FileOpTask import FileOpTask

class CopyTask(FileOpTask):
	def carryOut(self):
		copy(self.fromPath, self.toPath)
