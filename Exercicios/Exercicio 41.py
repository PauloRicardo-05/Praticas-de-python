from datetime import date
atual = date.today().year
ano_nasc = int(input("Digite seu ano de nascimento:"))
ano = atual - ano_nasc
if ano <= 9:
    print("Classificação: [MIRIM]")
elif ano > 9 <= 14:
    print("Classificação: [INFANTIL]")
elif ano > 14 <= 19:
    print("Classificação [JUNIOR]")
elif ano > 19 <= 25:
    print("Classificação [SÊNIOR]")
else:
    print("Classificação [MASTER]")