import requests
import socket
import geoip2.database
import os
import platform

def limpar(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

try:
    url = input("Digite um URL: ")

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    response = requests.get(url)

    domain = url.split("//")[-1].split("/")[0]
    dns = socket.gethostbyname_ex(domain)[-1][0]

    ip = socket.gethostbyname(domain)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    geoip_path = os.path.join(current_dir, "GeoLite2-Country.mmdb")

    reader = geoip2.database.Reader(geoip_path)
    country = reader.country(ip).country.name

    print(f"País: {country}")
    print(f"Ip: {ip}")
    print(f"Dns: {dns}")
    print(f"Info (Host): {domain}")

except requests.exceptions.MissingSchema:
    print("Informe um url válido, ex: https://www.google.com  / http://www.site.exemplo.com")

input('Pressione Enter para retomar ao menu principal: ')

limpar()
