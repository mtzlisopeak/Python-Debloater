from os import system
from subprocess import run

#função para verificar se algum dispositivo foi reconhecido
def verificar():
    verificacao = run("adb shell wm size")
    if verificacao.returncode == 1:
        print("Aparelho conectado")
    else:
        print("Nenhum dispositivo reconhecido")

verificar()
