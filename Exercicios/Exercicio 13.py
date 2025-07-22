salario = float(input("Digite seu salario: R$ "))
novo = salario + (salario * 15 / 100)
print("Seu novo salario com 15% de aumento será de : R${:.2f}".format(novo))