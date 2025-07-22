nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
média = (nota_1 + nota_2 )/ 2
if média < 5.0:
    print("[REPROVADO]Você não conseguiu atingir a média, a média exigida é 5, sua média foi de {}".format(média))
elif média > 7.0:
    print("[APROVADO]Parabéns, você foi aprovado com uma média de {}".format(média))
else:
    print("[RECUPERAÇÃO]Você não conseguiu atingir a média, a média exigida é 5, sua média foi de {}, você ficou de recuperação".format(média))