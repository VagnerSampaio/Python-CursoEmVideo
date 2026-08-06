from time import sleep

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} ate o {fim} de {passo} em {passo}")

    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1

    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(f'{contador} ', end='')
            sleep(0.1)
            contador += passo
        print('FIM')
    else:
        contador = inicio
        while contador >= fim:
            print(f'{contador} ', end='')
            sleep(0.1)
            contador -= passo
        print('FIM')

contador(1930,2026,4) #copas do mundo
contador(2050, 2026, 4)
contador(-5,10,1)

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)