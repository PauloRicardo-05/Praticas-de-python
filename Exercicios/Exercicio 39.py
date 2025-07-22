import time
print("O alistamento militar deve ser feito aos 18 anos")
idade = int(input("Digite sua idade:"))
ano_de_nascença = time.gmtime().tm_year-idade
print("Se você tem {} anos, então você nasceu em {}".format(idade,ano_de_nascença))
if idade > 18:
    print("Já passou da hora de se alistar! Você esta atrasado {} ano(s)".format(idade - 18))
elif idade <18:
    print("Ainda falta um pouco para o alistamento! Ainda falta {} ano(s)".format(18-idade))
else:
    print("Agora é a hora ! Esta exatamente na hora do alistamento obrigatório.")