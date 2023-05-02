@echo off

REM Verifica se o Python está instalado
where python > nul 2>&1
if %errorlevel% equ 0 (
  echo Python já está instalado.
) else (
  echo Instalando o Python...
  REM Faça o download da versão apropriada do Python em https://www.python.org/downloads/ e execute o instalador
  REM Certifique-se de adicionar o Python às variáveis de ambiente PATH durante a instalação
)

REM Instala os pacotes necessários
echo Instalando os pacotes necessários...
pip install -r requirements.txt

echo Concluído.
pause
