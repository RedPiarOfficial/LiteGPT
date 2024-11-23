import httpx
import re
import json
import sys
from .lib import AsyncHistory
from .lib.utils import Dtime
from .lib.exceptions import checkErrorStatus
import asyncio

class AsyncLiteGPT:
	def __init__(self, http2=False):
		self.http2 = http2
		self._checkPython()

	async def ask(self, prompt, history: AsyncHistory = None):
		if history is not None and type(history) is not AsyncHistory:
			return False

		if type(history) is AsyncHistory:
			history = history.history
			history.append({"role": "user", "content": str(prompt)})

		async with httpx.AsyncClient(http2=self.http2, timeout=30) as client:
			resp = await client.post("https://twitterclone-8wd1.onrender.com/api/chat",
									headers={
										"origin": "https://www.aiuncensored.info"
									},
									json={
										"cipher": await asyncio.to_thread(Dtime.rJ),
										"messages": [{"role": "user", "content": str(prompt)}] if history == None else history
									})
			checkErrorStatus(resp.status_code)
			extracted_elements = re.findall(r'data:\s*{\s*"data":\s*"(.*?)"\s*}', resp.text)
			combined_message = ''.join(json.loads(f'"{element}"') for element in extracted_elements)
			return combined_message

	async def image(self, prompt):
		async with httpx.AsyncClient(http2=self.http2, timeout=30) as client:
			resp = await client.post("https://twitterclone-4e8t.onrender.com/api/image",
									headers={
										"origin": "https://www.aiuncensored.info"
									},
									json={
										"cipher": await asyncio.to_thread(Dtime.rJ),
										"prompt": str(prompt)
									})
			checkErrorStatus(resp.status_code)
			return resp.json()

	def _checkPython(self):
		if sys.version_info <= (3, 8):
			print(f"[Warning AsyncLiteGPT] Async mode not supported python <= 3.8 (Your Version: {sys.version_info})")