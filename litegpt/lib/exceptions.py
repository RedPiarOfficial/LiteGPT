class ServiceUnavailable(Exception):
	def __init__(self):
		super().__init__("Error 503/502: The website is most likely undergoing maintenance. Please try again in a few minutes!")

class UnauthorizedError(Exception):
	def __init__(self):
		super().__init__("Authorization error! Please report this to the developer")

class TooManyRequests(Exception):
	def __init__(self):
		super().__init__("Too many requests, please try again in a few minutes!")

def checkErrorStatus(code):
	status = int(code)
	if status == 503 or status == 502:
		raise ServiceUnavailable
	elif status == 401:
		raise UnauthorizedError
	elif status == 429:
		raise TooManyRequests