n1=float(input("Digite o primeiro lado:  "))
n2=float(input("Digite o segundo lado:  "))
n3=float(input("Digite o terceiro lado:  "))
if n1+n2 > n3 and n2+n3>n1 and n1+n3 > n2:
    print("Este triangulo existe.")
    if n1==n2 and n1==n3:
        print("Ele é um traingulo EQUILÁTERO.")
    elif n1==n2 and n1 !=n3 or n1==n3 and n1!=n2:
        print("Ele é um triangulo ISÓSCELES.")
    else:
        print("Ele é um triangulo ESCALENO")
else:
    print("Não é possível formar um triangulo com essas medidas.")