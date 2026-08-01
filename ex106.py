from time import sleep

c = ("\033[m",        #0 = sem cor
     "\033[0;30;41m", #1 = vermelho
     "\033[0;30;42m", #2 = verde
     "\033[0;30;43m", #3 = amarelo
     "\033[0;30;44m", #4 = azul
     "\033[0;30;45m", #5 = roxo
     "\033[0;30;47m",    #6 = branco
     )

def ajuda(comando):
    titulo(f"Acessando o manual do comando {comando}", 4)
    print(c[6], end="")
    help(comando)
    print(c[0], end="")
    sleep(1)

def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~"*tam)
    print(f"  {msg}")
    print("~"*tam)
    print(c[0], end="")
    sleep(1)

comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYTHON",2)
    comando = str(input("\033[1;31mDigite uma comando:\033[m "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

titulo("ATÉ LOGO",1)