from os import system, chdir
from subprocess import run
from time import sleep
sair = False

#entra na pasta platform-tools
chdir("platform-tools")

#função para verificar se algum dispositivo foi reconhecido
def verificar():
    verificacao = run(["./adb", "shell", "wm", "size"])

    if verificacao.returncode == 0:
        limparTerminal()
        print("Dispositivo Conectado")
        desinstalarApp()

    elif verificacao.returncode == 1:
        limparTerminal()
        print("Nenhum dispositivo conectado")

def limparTerminal():
    system("clear")

def desinstalarApp():
    app = str(input("Nome do App:"))
    run(["./adb", "shell", "pm", "uninstall", "--user", "0", app])

def procurarApp():
    pacotes = run(["./adb", "shell", "pm", "list","packages"], text=True, capture_output=True).stdout.splitlines()

    limparTerminal()

    apps = [linha.replace("package:", "") for linha in pacotes]

    filtro = str(input("Digite o nome de um app que deseja:\n>>>"))

    for app in apps:
        if filtro in app:
            print(app)

while sair == False:

    limparTerminal()

    escolha = int(input("[ 0 ] Desinstalar App\n[ 1 ] Desativar App\n[ 2 ]Sair\n>"))
    
    if escolha == 0:
        pass
    elif escolha == 1:
        pass
    elif escolha == 2:
        limparTerminal()
        print("Byee")
        sleep(1)
        sair = True