numero = int(input("Digite qualquer numero:"))
opção = int(input("Qual será a base de conversão?\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n"))
if opção == 1:
    print("O numero {} convertido para binário é {}".format(numero,bin(numero)[2:]))
elif opção == 2:
    print("O numero {} convertido para octal é {}".format(numero,oct(numero)[2:]))
elif opção == 3:
    print("O numero {} convertido para hexadecimal é {}".format(numero,hex(opção)[2:]))
else:
    print("Não existe essa opção")