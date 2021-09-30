from asyncio import run, wait
from src.common.typing import VoidToCoroutine, VoidToNone
from typing import Coroutine, Iterable

def runAsyncOrSync(cond: bool, asyncFunc: VoidToCoroutine, syncFunc: VoidToNone):
	if cond:
		run(asyncFunc())
	else:
		syncFunc()

async def runCoros(coros: Iterable[Coroutine]):
	for task in (await wait(coros))[0]:
		try:
			print(task.result())
		except Exception as e:
			print(e)
