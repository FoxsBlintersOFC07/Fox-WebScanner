import os
import platform
from colorama import Fore
import time



#cria a função de limpar a tela
def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")

#SISTEMA DE MENU INICIAR
clear()
import os
import webbrowser

clear()

while True:
   print(f'''

{Fore.RED}◥█▀▀▀▀▀▀▀{Fore.LIGHTMAGENTA_EX} FOXS BLINTERS WEBMAP {Fore.RED}▀▀▀▀▀▀▀█◤
{Fore.LIGHTMAGENTA_EX}
  ___          ___  __              __  
 |__  __ |  | |__  |__)  |\/|  /\  |__) 
 |       |/\| |___ |__)  |  | /~~\ |    {Fore.RESET}

      \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m

{Fore.RED}◢█▄▄▄▄▄▄{Fore.LIGHTMAGENTA_EX} FOXS BLINTERS WEBMAP{Fore.RED} ▄▄▄▄▄▄▄▄█◣{Fore.RESET}
''');time.sleep(1.0)

   print(f'''
{Fore.RED}━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━━═━═━═━═


  {Fore.LIGHTYELLOW_EX}[01] {Fore.LIGHTMAGENTA_EX}Scanner de vuln. XSS   {Fore.LIGHTYELLOW_EX}[02] {Fore.LIGHTMAGENTA_EX}(IP) Escanear Portas Abertas 

  {Fore.LIGHTYELLOW_EX}[03] {Fore.LIGHTMAGENTA_EX} [INFO] Website        {Fore.LIGHTYELLOW_EX}[04] {Fore.LIGHTMAGENTA_EX}[INFO] IP 

  {Fore.RED}[00] {Fore.RED}SAIR {Fore.LIGHTYELLOW_EX}

{Fore.RED}━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━━═━═━═━═━{Fore.RESET}
''')

   escolha = input(f"{Fore.RED} ➥{Fore.MAGENTA}  ")

   if escolha == "1":
        clear()
        os.system("python src/xss.py")
   elif escolha == "2" or escolha == "02":
        clear()
        os.system("python src/ip.py")
   elif escolha == "3" or escolha == "03":
        clear()
        os.system("python src/website.py")
   elif escolha == "4" or escolha == "04":
        os.system("python src/ip_info.py")
        clear()
   elif escolha == "0" or escolha == "00":
        print('Obrigado por usar, Volte sempre!')
        exit()
   else:
        print("Opção incorreta")
        clear()