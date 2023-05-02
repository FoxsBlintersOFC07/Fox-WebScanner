import os
from colorama import Fore
import platform

def limpar(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

print(f''' {Fore.LIGHTMAGENTA_EX}
┏━────╯⌬╰────━┓
 {Fore.LIGHTRED_EX} XSS_SCANNER
 BY: Fox Waynne {Fore.LIGHTMAGENTA_EX}
┗━────╮⌬╭────━┛
{Fore.RESET}''')

pergunta = input(f"{Fore.MAGENTA}『Digite o URL do Site:』{Fore.BLUE} ")

fxss_hunter_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FXSS-Hunter')
os.chdir(fxss_hunter_path)

os.system(f'python FXSS-Hunter.py -u {pergunta}')

limpar()