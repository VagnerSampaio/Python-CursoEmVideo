num = int(input("Digite um valor: "))

#modulos
import aula22_modulos
fat = aula22_modulos.fatorial(num)
print(f"O fatorial de {num} é {fat}")

from aula22_modulos import dobro as d
print(f"O dobro de {num} é {d(num)}")

#pacotes (pastas)
from aula22_pacotes import numeros as n
print(f"O triplo de {num} é {n.triplo(num)}")