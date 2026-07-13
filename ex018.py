from math import radians, sin, cos, tan
an = float(input("Digite um angulo que voce deseja: "))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print("O angulo {} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}".format(an, seno, cos, tan))
