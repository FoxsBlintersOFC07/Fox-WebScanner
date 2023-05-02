
from lib.helper.helper import * 
from datetime import datetime
class Log:

	@classmethod
	def info(self,text):
 		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+G+"INFORMAÇÕES"+N+"] "+text)
 
	@classmethod
	def warning(self,text):
		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+Y+"ALERTA"+N+"] "+text)

	@classmethod
	def high(self,text):
 		print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+R+"CRÍTICO"+N+"] "+text)
 		