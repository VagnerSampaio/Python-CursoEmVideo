times = ("Corinthians", "Palmeias", "Santos", "Grêmio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atlético-PR", "Bahia",
         "São Paulo", "Fluminense", "Sport Recife",
         "EC Vitória", "Coritiba", "Avaí", "Ponte Preta",
         "Atlético-GO")

for pos, time in enumerate(times):
    print(f"{pos} - {time}")

print("-=" * 15)
print(f"Lista de time: {times}")
print("-=" * 15)
print("O 5 primeiros times da tabela:", times[0:5])
print("-=" * 15)
print("O 5 ultimos times da tabela:", times[-5:])
print("-=" * 15)
print(f"Times em ordem alfabetica: {sorted(times)}")
print("-=" * 15)
print(f"O Chapecoense está na {times.index("Chapecoense")+1}a posição")