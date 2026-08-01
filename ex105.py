def notas(*n, sit=False):
    """
    Funcao para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas para alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao no retorno
    :return: dicionario com varias informacoes sobre a situacao do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['sit'] = "Aprovado"
        elif r['media'] >= 5:
            r['sit'] = "Recuperacao"
        else:
            r['sit'] = "Reprovado"
    return r

help(notas)
resp = notas(5.5, 2.5, 8.5, sit = True)
print(resp)
