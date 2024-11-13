class History:
	def __init__(self):
		self._history = []

	def add(self, role, content):
		self._history.append({"role": str(role), "content": str(content)})
		return True

	def remove(self, index=-1):
		self._history.pop(index)
		return self._history

	def insert(self, data: dict):
		if type(data) is list:
			for i in data:
				self.add(i[0], i[1])
			return True
		return {"Error": "Data type must is List."}

	@property
	def history(self):
		return self._history

	def __repr__(self):
		return str(self._history)