import argparse
import socket
import threading
import os
from colorama import Fore

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = socket.getservbyport(port)
            print(f"{Fore.RED}Porta: {Fore.RESET}{Fore.LIGHTYELLOW_EX} {port} {Fore.RESET}{Fore.RED} | Serviço: {Fore.LIGHTYELLOW_EX}{service}{Fore.RESET}")
        sock.close()
    except:
        pass

def scan(ip, start_port, end_port):
    print(f"{Fore.BLUE}Escaneando IP: {Fore.YELLOW}{ip}{Fore.RESET}")
    for port in range(start_port, end_port+1):
        threading.Thread(target=check_port, args=(ip, port)).start()

def main():
    parser = argparse.ArgumentParser(description="Scanner de portas")
    parser.add_argument('-ip', '--ip_address', help='Endereço IP para escanear', required=True)
    args = parser.parse_args()
    ip_address = args.ip_address
    start_port = 10
    end_port = 10000
    clear_screen()
    scan(ip_address, start_port, end_port)
    input("Scanner concluído! Pressione enter para sair.")
    # Voltando para a pasta anterior
    os.chdir('..')
    os.chdir('..')
    clear_screen()
    os.system('python main.py')
    

if __name__ == '__main__':
    main()
