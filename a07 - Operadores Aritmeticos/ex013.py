salario = float(input("Qual o salário do funcionário? R$"))
novo = salario + (salario * 15/100)

print("Um funcionário que ganhava R${}, com 15% de aumento passa a receber R${}.".format(salario, novo))