echo Carpeta de Instalacion de dependencias

cd /d %~dp0
@echo off
cd %

@echo on
echo pip3 install requests
pip3 install pandas
echo en caso de repetir instalacion pip3 uninstall matplotlib
python3 -m pip install --upgrade pip
pip3 install matplotlib

python -m pip install --upgrade pip
echo para la instalación correcta
python3 -m pip install matplotlib --user

echo END
PAUSE