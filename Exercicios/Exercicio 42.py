r1 = float(input("Digite a primeira reta:"))
r2 = float(input("Digite a segunda reta:"))
r3 = float(input("Digite a terceira reta:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas informadas podem fazer um triângulo ", end="")
    if r1 != r2 != r3 != r1:
        print("As retas formam um triãngulo Escaleno!")
    elif r1 == r2 == r3:
        print("As retas formam um triângulo Equilátero!")
    else :
        print("As retas formam um triângulo Isóceles")
else:
    print("As retas a cima não podem formar um triângulo!")