import os
from colorama import Fore
print(f''' {Fore.LIGHTMAGENTA_EX}
┏━────╯⌬╰────━┓
 {Fore.LIGHTRED_EX}  IP SCANNER 
 BY: Fox Waynne {Fore.LIGHTMAGENTA_EX}
┗━────╮⌬╭────━┛
{Fore.RESET}''')
pergunta = input(f"{Fore.MAGENTA}『Digite o Endereço de ip que deseja Escanear:』{Fore.BLUE} ")
ip_info_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'IpScanner')
os.chdir(ip_info_path)
os.system(f'python ipscanner.py -ip {pergunta}')