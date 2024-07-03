from os import system, chdir
from subprocess import run

#entra na pasta platform-tools
chdir("platform-tools")

#função para verificar se algum dispositivo foi reconhecido
def verificar():
    verificacao = run(["./adb", "shell", "wm", "size"])
    if verificacao.returncode == 0:
        system("clear")
        print("Conectado")
    elif verificacao.returncode == 1:
        system("clear")
        print("Não conectado")

verificar()
