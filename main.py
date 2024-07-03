from os import system, chdir
from subprocess import run
from time import sleep

#entra na pasta platform-tools
chdir("platform-tools")

#função para iniciar o programa e verifica se tem algum dispositivo conectado no computador
def iniciar():
    sair = False
    verificacao = run(["./adb", "shell", "wm", "size"])

    if verificacao.returncode == 0:
        limparTerminal()
        while sair == False:
            
            escolha = input("[ 1 ] Desinstalar App\n[ 2 ] Desativar App\n[ E ] Sair\n>>>")
            
            if escolha == "1":
                desinstalarApp()

            elif escolha == "2":
                desativarApp()

            elif escolha == "E" or escolha == "e":
                print("Byee")
                sleep(1)
                limparTerminal()
                sair = True

            else:
                limparTerminal()
                print("Opção inválida")

    elif verificacao.returncode == 1:
        limparTerminal()
        print("Nenhum dispositivo conectado")

def limparTerminal():
    system("clear")

def desinstalarApp():
    while True:
        limparTerminal()

        procurarApp()
        app = input("Digite o nome do app a ser deinstalado ou aperte [E] para sair:\n>>>")
        if app == "E" or app == "e":
            break

        else:
            desinstalacao = run(["./adb", "shell", "pm", "uninstall", "--user", "0", app])
            if desinstalacao.returncode == 0:
                limparTerminal()
                print("Desinstalado com sucesso")

            else:
                limparTerminal()
                print("Falha na desinstalação")
            
            sleep(1)
            limparTerminal()

def desativarApp():
    while True:
        limparTerminal()

        procurarApp()
        app = str(input("Digite o nome do app a ser desativado ou aperte [ E ] para sair:\n>>>")).lower()
        if app == "E" or app == "e":
            break
        else:
            desativacao = run(["./adb", "shell", "pm", "disable-user", "--user", "0", app])
            if desativacao.returncode == 0:
                limparTerminal()
                print("Desativado com seucesso")

            else:
                limparTerminal()
                print("Falha na desinstalação")

        sleep(1)
        limparTerminal()

def procurarApp():
    pacotes = run(["./adb", "shell", "pm", "list","packages"], text=True, capture_output=True).stdout.splitlines()
    apps = [package.replace("package:", "") for package in pacotes]
    limparTerminal()

    filtro = str(input("Digite o nome de um app que deseja procurar:\n>>>"))
    apps_filtrados = [app for app in apps if filtro in app]

    if not apps_filtrados:
        print("Nenhum app encontrado")
    else:
        for app in apps_filtrados:
            print(app)

iniciar()
