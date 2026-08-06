def voto(ano):
    from datetime import date #impotacao dentro da funcao
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 18 < idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
         return f"Com {idade} anos: VOTO OBRIGATORIO."

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))