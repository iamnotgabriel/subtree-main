import json
from datetime import datetime

class Logger:
	def __init__(self, context):
		self.context = context

	def __log(self, **kargs):
		kargs["context"] = self.context
		kargs["at"] = datetime.now().isoformat()
		print(json.dumps(kargs))
		
	def log(self, **kargs):
		kargs["level"] = "LOG"
		self.__log(**kargs)
