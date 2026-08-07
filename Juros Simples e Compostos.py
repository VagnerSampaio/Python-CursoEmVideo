#"Os juros compostos são a oitava maravilha do mundo.
#Aquele que entende, ganha; Quem não entende, paga."
#Albert Einstein
taxa_juros = float(input("Taxa de juros anual (%): ")) / 100
tempo = int(input("Tempo de investimento (anos): "))
capital_inicial = float(input("Valor do aporte inicial (R$): "))

juros_simples = capital_inicial * taxa_juros * tempo
juros_compostos = capital_inicial * ((1 + taxa_juros) ** tempo)

print()
print(f"Juros Simples: R${juros_simples:.2f}, isso rende R${juros_simples/100:.2f} ao mês.")
print(f"Juros Compostos: R${juros_compostos:.2f}, isso rende R${juros_compostos/100:.2f} ao mês.")