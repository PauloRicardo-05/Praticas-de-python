salario = float(input("Digite seu salario para o calculo do aumento:"))

if salario > 1250.00 :
    aumento = salario * 0.10
    salario = salario + aumento
    print("Seu novo salario é: R${:.2f}".format(salario))
else :
    aumento = salario * 0.15
    salario = salario+ aumento
    print("Seu novo salario é: R${:.2f}".format(salario))
    