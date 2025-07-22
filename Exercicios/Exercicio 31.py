viagem = float(input("Qual a distância em km da sua viagem ?\n"))
if viagem <=200:
    mult = viagem*0.50
else:
    mult = viagem*0.45
print("O valor da viagem é de \nR${:.2f}".format(mult))