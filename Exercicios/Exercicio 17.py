from math import sqrt,pow  
op = float(input("Digite o cateto oposto: "))
ad = float(input("Agora o Adjascente: "))
print("A hipotenusa vale {:.2f}".format(sqrt(op**2+ad**2)))