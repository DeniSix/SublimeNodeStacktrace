from . import logger

log = logger.get('clicks')

class Clicks(object):
	def __init__(self):
		self._clicks = []
		self._prev = None

	def add(self, region, callback, data):
		log('add', region, callback, data)
		self._clicks.append({'region': region, 'callback': callback, 'data': data})

	def check(self, cursor):
		log('click', cursor == self._prev, cursor, self._prev)
		if cursor == self._prev:
			return
		self._prev = cursor
		for click in self._clicks:
			if cursor > click['region'].a and cursor < click['region'].b:
				click['callback'](click['data'])
