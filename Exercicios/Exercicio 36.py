valor_da_casa = float(input("Qual o valor da casa? \n:R$"))
salario = float(input("Qaul o seu salário ? \n:R$"))
tempo = int(input("Em quantos anos você ira pagar ? \n:"))

prestacao = (valor_da_casa / (tempo * 12))

print("Neste caso, o valor das prestações de uma casa de R${:.2f} para pagar em {} anos serão de R$ {:.2f}" .format(valor_da_casa,tempo,prestacao))
if prestacao <= (salario*30/100):
    print("Parabéns, seu empréstimo foi concedido !")
else:
    print("Neste caso você não poderá realizar um empréstimo")
