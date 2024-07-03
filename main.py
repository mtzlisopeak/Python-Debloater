from os import system, chdir
from subprocess import run
from time import sleep
sair = False

#entra na pasta platform-tools
chdir("platform-tools")

#função para verificar se algum dispositivo foi reconhecido
def verificar():
    global sair
    verificacao = run(["./adb", "shell", "wm", "size"])

    if verificacao.returncode == 0:
        limparTerminal()
        while sair == False:
            limparTerminal()
            escolha = int(input("[ 0 ] Desinstalar App\n[ 1 ] Desativar App\n[ 2 ]Sair\n>>>"))
            
            if escolha == 0:
                desinstalarApp()

            elif escolha == 1:
                break

            elif escolha == 2:
                limparTerminal()
                print("Byee")
                sleep(1)
                sair = True

            else:
                print("Opção inválida")

    elif verificacao.returncode == 1:
        limparTerminal()
        print("Nenhum dispositivo conectado")

def limparTerminal():
    system("clear")

def desinstalarApp():
    procurarApp()
    app = str(input("Desinstalar o App:"))
    run(["./adb", "shell", "pm", "uninstall", "--user 0", app])
    sleep(1)
    while True:
        limparTerminal()
        continuar = int(input("[ 0 ] Desinstalar outro App\n[ 1 ] Sair\n>>>"))
        if continuar == 0:
            desinstalarApp()
        
        elif continuar == 1:
            break

        else:
            print("Opção inválida")
            sleep(1)

def procurarApp():
    pacotes = run(["./adb", "shell", "pm", "list","packages"], text=True, capture_output=True).stdout.splitlines()

    limparTerminal()

    apps = [package.replace("package:", "") for package in pacotes]

    filtro = str(input("Digite o nome de um app que deseja procurar:\n>>>"))

    for app in apps:
        if filtro in app:
            print(app)

verificar()