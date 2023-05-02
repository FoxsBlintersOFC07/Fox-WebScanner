import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint
from lib.crawler.crawler import *
import os

def menu_principal():
	os.chdir('..')
	os.chdir('..')
	os.system('python main.py')


def check(getopt):
	payload=int(getopt.payload_level)
	if payload > 6 and getopt.payload is None:
		Log.info("Deseja usar um Payload Customizado?(Y/n)?")
		answer=input("> "+W) 
		if answer.lower().strip() == "y":
			Log.info("Escreva um Payload XSS abaixo:")
			payload=input("> "+W)
		else:
			payload=core.generate(randint(1,6))
	
	else:
		payload=core.generate(payload)
			
	return payload if getopt.payload is None else getopt.payload
	
def start():
	parse=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,usage="FXSS-Hunter -u <alvo> [Opções]",add_help=False)
	
	pos_opt=parse.add_argument_group("Opções")
	pos_opt.add_argument("--help",action="store_true",default=False,help="Mostra os parâmetros de ajuda e uso")
	pos_opt.add_argument("-u",metavar="",help="URL de destino (por exemplo, http://testphp.vulnweb.com)")
	pos_opt.add_argument("--depth",metavar="",help="Profundidade da página da web para rastrear. Padrão: 2",default=2)
	pos_opt.add_argument("--payload-level",metavar="",help="Nível do gerador de payload, 7 para payload personalizado. {1...6}. Padrão: 6",default=6)
	pos_opt.add_argument("--payload",metavar="",help="Carregue um payload personalizado diretamente (por exemplo, <script>alert(2005)</script>)",default=None)
	pos_opt.add_argument("--method",metavar="",help="Configuração do método:\n\t0: GET\n\t1: POST\n\t2: GET e POST (padrão)",default=2,type=int)
	pos_opt.add_argument("--user-agent",metavar="",help="Agente do usuário da solicitação (por exemplo, Chrome/2.1.1/...)",default=agent)
	pos_opt.add_argument("--single",metavar="",help="Digitalização única. Sem rastreamento, apenas um endereço")
	pos_opt.add_argument("--proxy",default=None,metavar="",help="Definir proxy (por exemplo, {'https':'https://10.10.1.10:1080'})")
	pos_opt.add_argument("--about",action="store_true",help="Imprime informações sobre a ferramenta F-XSS")
	pos_opt.add_argument("--cookie",help="Definir cookie (por exemplo, {'ID':'1094200543'})",default='''{"ID":"1094200543"}''',metavar="")
	
	getopt=parse.parse_args()
	print(logo)
	Log.info("Iniciando o FXSS-Hunter...")
	if getopt.u:
		core.main(getopt.u,getopt.proxy,getopt.user_agent,check(getopt),getopt.cookie,getopt.method)
		
		crawler.crawl(getopt.u,int(getopt.depth),getopt.proxy,getopt.user_agent,check(getopt),getopt.method,getopt.cookie)
		
	elif getopt.single:
		core.main(getopt.single,getopt.proxy,getopt.user_agent,check(getopt),getopt.cookie,getopt.method)
		
	elif getopt.about:
		print("""
***************
Projeto: FXSS-Hunter
License: MIT
Autor: Fox Waynne & Foxs Blinters Legion
(Ferramenta baseada no PwnXSS, crétidos ao criador da mesma)
****************
""")
	else:
		parse.print_help()
		
if __name__=="__main__":
	start()
	input("Scanner concluído! Pressione enter para sair.")
	menu_principal()