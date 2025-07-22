preco = int(input("Digite o valor a ser pago: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão")
opção = int(input("Qual é a sua opção ? "))
if opção == 1:
    print("Você recebeu um desconto de 10%, logo você só pagará R${:.f}".format(preco-(10/100)*preco))
elif opção == 2:
    print("Você recebeu um desconto de 5%, logo você pagará R${:.f}".format(preco-(5/100)*preco))
elif opção == 3:
    print("Sua compra dividida em 2x no cartão fica R${:.f}".format(preco/2))
elif opção == 4:
    parcelas = int(input("Quantas parcelas ? "))
    preco_novo = preco + (20 / 100) * preco
    print("Sua compra dividia em {} parcelas adiciona um juros de 20%\nLogo {}x de R${:.f}, da um total de R${:.f} ".format(parcelas,parcelas,preco_novo/parcelas,preco_novo))
else:
    print("Opção invalida, tente novamente")