from src.common.fileOps import purge
from src.common.FileOpTask import FileOpTask

class MoveTask(FileOpTask):
	def carryOut(self):
		try:
			self.fromPath.rename(self.toPath)
		except FileExistsError:
			purge(self.fromPath)
