n1=int(input("Digite um número:"))
n2=int(input("Digite um segundo número:"))
if n1==n2:
    print(f"Digite um número diferente de {n1}")

n3=int(input("Digite um terceiro número:"))
if n1==n3:
    print(f"Digite um número diferente de {n1}")
elif n2==n3:
    print (f"Digite um número diferente de {n2}")
if n1 != n2 and n1 != n3 and n2 != n3:
    if n2 > n1 and n2 > n3 and n3>n1:
        maior=n2
        menor=n1
    elif n2>n1 and n2>n3 and n1>n3:
        maior=n2
        menor=n3
    elif n3>n1 and n3>n2 and n1>n2 :
        maior=n3
        menor=n2
    elif n3>n1 and n3>n2 and n2>n1:
        menor=n1
        maior=n3
    elif n1>n2 and n1>n3 and n2>n3:
     maior=n1
     menor=n3
    elif n1>n2 and n1>n3 and n3>n2:
        maior=n1
    menor=n2
    
    print(f"O maior valor entre os tres é {maior}")
    print(f"O menor número dentre os tres é {menor}")
      
