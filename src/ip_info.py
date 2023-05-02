import requests
import platform
import os

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")

clear()

ip = input("\033[1;91m Digite o endereço IP: \033[1;92m")

url = "https://ipapi.co/{}/json/".format(ip)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('\n\033[32;1m ⟾IP ENCONTRADO⟽\033[0;0m')
    print('\n\033[34;1m◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n◆-')
    print(f"\033[34;1m➢País: \033[0;0m\033[37;1m{data['country_name']}")
    print(f"\033[34;1m➢Estado: \033[0;0m\033[37;1m{data['region']}")
    print(f"\033[34;1m➢Cidade: \033[0;0m\033[37;1m{data['city']}")
    print(f"\033[34;1m➢Código postal: \033[0;0m\033[37;1m{data['postal']}")
    print(f"\033[34;1m➢Latitude: \033[0;0m\033[37;1m{data['latitude']}")
    print(f"\033[34;1m➢Longitude: \033[0;0m\033[37;1m{data['longitude']}")
    print(f"\033[34;1m➢Fuso horário: \033[0;0m\033[37;1m{data['timezone']}")
    print(f"\033[34;1m➢ISP: \033[0;0m\033[37;1m{data['org']}")
    print(f"\033[34;1m➢AS: \033[0;0m\033[37;1m{data['asn']}")
    print(f"\033[34;1m➢Moeda: \033[0;0m\033[37;1m{data['currency']}")
    print(f"\033[34;1m➢Capital do país: \033[0;0m\033[37;1m{data['country_capital']}")
    print(f"\033[34;1m➢População do país: \033[0;0m\033[37;1m{data['country_population']}")
    print(f"\033[34;1m➢Nome da moeda: \033[0;0m\033[37;1m{data['currency_name']}")
    print(f"\033[34;1m➢Código da região: \033[0;0m\033[37;1m{data['region_code']}")
    print(f"\033[34;1m➢Código do país: \033[0;0m\033[37;1m{data['country']}")
    print(f"\033[34;1m➢Código do país ISO3: \033[0;0m\033[37;1m{data['country_area']}")
    print(f"\033[34;1m➢Área do país: \033[0;0m\033[37;1m{data['country_tld']}")
    print(f"\033[34;1m➢TLD do país: \033[0;0m\033[37;1m{data['country_calling_code']}")
    print(f"\033[34;1m➢Código de área: \033[0;0m\033[37;1m{data['country_area']}")
    print('\033[34;1m◆-\n◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆')
else:
    print("\n\033[32;1m ⟾Não foi possível obter informações sobre o IP informado.⟽\033[0;0m")

input('\033[1;91m Pressione Enter para voltar ao menu: \033[1;92m')

