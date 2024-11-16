import httpx
import re
import json
import logging

from .lib import History
from .lib.exceptions import checkErrorStatus
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
class LiteGPT:
	def __init__(self, http2=False):
		self.requests = httpx.Client(http2=http2)

	def ask(self, prompt, history: History = None):
		if history is not None and type(history) is not History:
			logging.warning("Передано недопустимое значение для 'history': ожидался тип 'History' или значение не должно быть None.")
			return False
		pattern = r'data:\s*{\s*"data":\s*"(.*?)"\s*}'
		
		if type(history) is History:
			history = history.history
			history.append({"role": "user", "content": str(prompt)})

		resp = self.requests.post("https://twitterclone-8wd1.onrender.com/api/chat",
									timeout=30,
									headers={
												"origin": "https://www.aiuncensored.info",
											},
									json={
											"cipher": "0000000000000000",
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
											"cipher": "0000000000000000",
											"prompt": str(prompt)
										}
									)
		checkErrorStatus(resp.status_code)
		return resp.json()