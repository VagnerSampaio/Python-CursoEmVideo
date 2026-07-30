from time import sleep
def maior(*numeros):
    contador = maior = 0

    for valor in numeros:
        sleep(0.1)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f"Foram informados {contador} valores, maior valor informado foi {maior}")


maior(2,9,4,5,7,1)
maior(4,7,1)
maior(1,2)
maior(6)
maior()