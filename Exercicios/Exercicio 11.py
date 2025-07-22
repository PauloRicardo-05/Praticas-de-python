largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede: "))
area = largura*altura 
lit = area/2
print("Sua area é de ", area,"m²")
print("para cada m² de area será necessário 2 litros de tinta")
print("Logo, para {}m² será utilizado {} litros de tinta".format(area,lit))