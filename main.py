from os import system, chdir
from subprocess import run

#entra na pasta platform-tools
chdir("platform-tools")

#função para verificar se algum dispositivo foi reconhecido
def verificar():
    verificacao = run(["./adb", "shell", "wm", "size"])
    if verificacao.returncode == 0:
        system("clear")
        print("Dispositivo Conectado")
        desinstalarApp()
    elif verificacao.returncode == 1:
        system("clear")
        print("Nenhum dispositivo conectado")

def desinstalarApp():
    run(["./adb", "shell", "pm", "list", "packages"])
    app = str(input("Nome do App:"))
    run(["./adb", "shell", "pm", "uninstall", "--user", "0", app])
    
verificar()
