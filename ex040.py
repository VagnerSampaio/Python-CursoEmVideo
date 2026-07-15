nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Tirando {:.2f} e {:.2f}, a media do aluno é {:.2f}".format(nota1, nota2, media))

if media >= 7:
    print("Aprovado")
elif 7 > media >= 5:
    print("Recuperacao")
else:
    print("Reprovado")