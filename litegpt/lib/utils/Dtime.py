from datetime import datetime, timezone

def rJ():
	now = datetime.now(timezone.utc)  # Получаем текущее время в UTC с учетом часового пояса
	e = str(now.day).zfill(2)  # День месяца с ведущим нулем
	t = str(now.hour).zfill(2)  # Часы с ведущим нулем
	r = str(now.minute).zfill(2)  # Минуты с ведущим нулем
	o = str(now.year)[2:]  # Последние две цифры года
	return e + t + r + o  # Объединяем в строку