#python.org > documentation > library reference
import random #importar biblioteca inteira
from math import sqrt, ceil #importar somente funcoes da biblioteca
import emoji

num = random.randint(1, 100)
raiz = sqrt(num)

print("A raiz de {} é igual a {:.2f}".format(num, raiz))