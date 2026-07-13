nome = "Joao Vagner de Alencar Sampaio"
print(nome)

print(len(nome), "caracteres.")

print(nome[0],nome[5],nome[15],nome[23])
print(nome[5:11])
print(nome[:4], nome[23:])
print(nome[0::2]) #pulando de 2 em 2

print(nome.count('A')+nome.count('a'), "letras 'A/a'.")
print(nome.find("Android")) #não tem string Android
print("de" in nome, "Tem 'de' no nome")
print(nome.replace(" ","-"))

print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())

print(nome.strip()) #remover espaços antes e depois da string
print(nome.rstrip()) #remover somente lado direito
print(nome.lstrip()) #remover somente lado esquerdo

splitado = nome.split()
print(splitado)
print('-'.join(splitado))
print('-'.join(nome))

print("""
O Python é uma linguagem de programação  amplamente usada em aplicações da Web,
desenvolvimento de software, ciência de dados e machine learning (ML). Os
desenvolvedores usam o Python porque é eficiente e fácil de aprender e pode ser
executada em muitas plataformas diferentes.
""") ##print formatado
