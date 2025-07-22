import math
angulo = float(input("Digite o Ângulo que deseja: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("Seu SENO é {:.2f}".format(seno))
print("Seu COSSENO é {:.2f}".format(cos))
print("Sua TANGENTE é {:.2f}".format(tan))