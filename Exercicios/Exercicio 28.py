from random import randint
pc = randint(0,5) #PC esta pensando esse safado
print("Estou pensando em um numero de 0 a 5, tente adivinhar...")
print("-"*20)
player = int(input("Qual numero eu pensei ? \n:")) #O player burro tenta acertar
print("-"*20)
if player == pc:
    print("Você acertou")
else:
    print("Você errou, pensei no numero {}, e não no {}".format(pc, player))
