import json
import sys
from datetime import datetime

class Logger:
	def __init__(self, context):
		self.context = context

	def __log(self,file=sys.stdout, **kargs):
		kargs["context"] = self.context
		kargs["at"] = datetime.now().isoformat()
		print(json.dumps(kargs), file=file)
		
	def log(self, **kargs):
		kargs["level"] = "LOG"
		self.__log(**kargs)

	def error(self, **kargs):
		kargs["level"] = "ERROR"
		self.__log(file=sys.stderr,**kargs)
