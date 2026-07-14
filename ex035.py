r1 = int(input("Digite o primeiro lado do triangulo: "))
r2 = int(input("Digite o segundo lado do triangulo: "))
r3 = int(input("Digite o terceiro lado do triangulo: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os valores acima podem formar um triangulo")
else:
    print("Os valores acima não podem formar um triangulo")
