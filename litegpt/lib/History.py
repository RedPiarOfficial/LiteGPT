import os
import json
from typing import Union

class History:
	def __init__(self):
		self._history = []

	def add(self, role, content):
		self._history.append({"role": str(role), "content": str(content)})
		return True

	def remove(self, index=-1):
		self._history.pop(index)
		return self._history

	def insert(self, data: list):
		if type(data) is list:
			for i in data:
				self.add(i[0], i[1])
			return True
		return {"Error": "Data type must is List."}

	def save(self, path: Union[str, os.PathLike] = "./AutoHistory.json") -> bool:
		dir_path = os.path.dirname(path)
		
		if dir_path:
			os.makedirs(dir_path, exist_ok=True)
		
		try:
			with open(path, "w", encoding="utf-8") as file:
				json.dump(self._history, file, ensure_ascii=False, indent=4)
			return True
		except (OSError, json.JSONDecodeError) as e:
			print(f"Error: {e}")
			return False

	def load(self, path: Union[str, os.PathLike] = "./AutoHistory.json") -> bool:
		try:
			with open(path, "r", encoding="utf-8") as file:
				self._history = json.load(file)
				return True
		except FileNotFoundError:
			return False

	@property
	def history(self):
		return self._history

	def __repr__(self):
		return str(self._history)