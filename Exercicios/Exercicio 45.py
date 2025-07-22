from random import randint
from time import sleep
from traceback import print_tb

itens = ("Pedra","Papel","Tesoura")
pc = randint (0,2)
print("Opções\n [0] Pedra\n [1] Papel\n [2]Tesoura ")
jg = int(input("Escolha uma opção: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("-=" * 10)
print("O computador escolheu {}".format(itens[pc]))
print("O jogador escoleu {}".format(itens[jg]))
print("-=" * 10)
if pc == 0:
    if jg == 0:
        print("EMPATE")
    elif jg == 1:
        print("JOGADOR VENCE")
    elif jg == 2:
        print(("COMPUTADOR VENCE"))
    else:
        print("JOGADA INVÁLIDA")
elif pc == 1:
    if jg == 0:
        print("COMPUTADOR VENCE")
    elif jg == 1:
        print("EMPATE")
    elif jg == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")

elif pc == 2:
    if jg == 0:
        print("JOGADOR VENCE")
    elif jg == 1:
        print("COMPUTADOR VENCE")
    elif jg == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")

