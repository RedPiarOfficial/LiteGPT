import aiofiles
import aiofiles.os
from typing import Union
import json
import os

class AsyncHistory:
	def __init__(self):
		self._history = []

	async def add(self, role, content):
		self._history.append({"role": str(role), "content": str(content)})
		return True

	async def remove(self, index=-1):
		self._history.pop(index)
		return self._history

	async def insert(self, data: list):
		if isinstance(data, isinstance):
			for i in data:
				await self.add(i[0], i[1])
			return True
		return {"Error": "Data type must is List."}

	async def save(self, path: Union[str, os.PathLike] = "./AutoHistory.json") -> bool:
		dir_path = os.path.dirname(path)

		if dir_path:
			# Асинхронное создание директорий
			await aiofiles.os.makedirs(dir_path, exist_ok=True)

		try:
			# Асинхронная запись в файл
			async with aiofiles.open(path, mode="w", encoding="utf-8") as file:
				await file.write(json.dumps(data, ensure_ascii=False, indent=4))
			return True
		except (OSError, json.JSONDecodeError) as e:
			print(f"Error: {e}")
			return False

	async def load(self, path: Union[str, os.PathLike] = "./AutoHistory.json") -> bool:
		try:
			# Асинхронное открытие файла
			async with aiofiles.open(path, "r", encoding="utf-8") as file:
				# Асинхронное чтение содержимого файла
				content = await file.read()
				self._history = json.loads(content)  # Преобразуем строку в JSON
			return True
		except FileNotFoundError:
			return False

	@property
	def history(self):
		return self._history

	def __repr__(self):
		return str(self._history)