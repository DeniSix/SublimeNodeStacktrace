
# List of modules you want to see log to
debuggee = [
	# 'debug_client',
	# 'cmd_attach_debugger',
	# 'cmd_start_debugger',
	# 'clicks',
]

def get(name):
	def log(*args):
		if name in debuggee:
			print('[NDBG][%s]%s' % (name, args))
	return log
