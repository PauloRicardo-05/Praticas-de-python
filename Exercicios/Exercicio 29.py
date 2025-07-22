vel = float(input("Qual a velocidade atual do seu carro ?\n:"))
if vel > 80:
    multa = (vel-80)*7
    print("Você esta acima da velocidade permitida que é 80km/h, você será multado em:\nR${:.2f}".format(multa))
else:
    print("Tenha uma ótima viagem e diriga com cuidado")
    
#{:.2f} --> é chato mas é util