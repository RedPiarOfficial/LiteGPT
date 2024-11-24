import httpx
import re
import json
import random

from .lib import History
from .lib.exceptions import checkErrorStatus
from .lib.utils import Dtime

class LiteGPT:
	def __init__(self, http2=False):
		self.requests = httpx.Client(http2=http2)

	def ask(self, prompt, history: History = None):
		if history is not None and type(history) is not History:
			return False
		pattern = r'data:\s*{\s*"data":\s*"(.*?)"\s*}'
		
		if type(history) is History:
			history = history.history
			history.append({"role": "user", "content": str(prompt)})
		resp = self.requests.post("https://twitterclone-8wd1.onrender.com/api/chat",
									timeout=30,
									headers={"origin": "https://www.aiuncensored.info"},
									json={
											"cipher": Dtime.rJ(),
											"messages": [{"role": "user", "content": str(prompt)}] if history == None else history
										}
									)
		extracted_elements = re.findall(pattern, resp.text)
		combined_message = ''.join(json.loads(f'"{element}"') for element in extracted_elements)
		checkErrorStatus(resp.status_code)
		return combined_message

	def image(self, prompt):
		resp = self.requests.post("https://twitterclone-4e8t.onrender.com/api/image",
									timeout=30,
									headers={"origin": "https://www.aiuncensored.info"},
									json={
											"cipher": Dtime.rJ(),
											"prompt": str(prompt)
										}
									)
		checkErrorStatus(resp.status_code)
		return resp.json()