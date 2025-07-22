num = int(input("Digite um numero para ver se é par ou impar:\n"))
re = num % 2 #aqui eu divido o numeo por 2 massss o "%" me retorna só o resto, ou seja, 1
if re == 1:
    print("É impar")
else: 
    print("É par")