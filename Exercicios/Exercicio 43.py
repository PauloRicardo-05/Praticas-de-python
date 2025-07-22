peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
IMC = peso/(altura**2)
print("Seu IMC (indice de massa corporal) é {:.2f}".format(IMC))
if IMC < 18.5:
    print("Você esta abaixo do peso")
elif 18.5 <= IMC < 25:
    print("Você esta com peso ideal")
elif 25 <= IMC < 30:
    print("Você esta com Sobrepeso")
elif 30 <= IMC < 40:
    print("Você esta com Obesidade")
elif IMC >= 40:
    print("Você esta com Obesidade Mórbida")