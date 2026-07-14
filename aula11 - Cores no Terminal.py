#style
#0 = none
#1 = bold
#4 = underline
#7 = negative

#colors
#30 to 37

#back
#40 to 47

print("\033[0:30:41mTeste\033[m")
print("\033[4:33:44mTeste\033[m")
print("\033[1:35:43mTeste\033[m")
print("\033[30:42mTeste\033[m")
print("\033[mTeste\033[m")
print("\033[7:30mTeste\033[m")

nome = "Vagner Sampaio"
print("Olá! Muito prazer em te conhecer,{}{}{}!".format("\033[4:33:44m", nome, "\033[m"))

cores = {
    "limpa": "\033[m",
    "azul": "\033[1;34m",
    "amarelo": "\033[1;33m",
    "pretoebranco": "\033[7;30m"
}

print("Olá! Muito prazer em te conhecer,{}{}{}!".format(cores["azul"], nome, cores["limpa"]))
