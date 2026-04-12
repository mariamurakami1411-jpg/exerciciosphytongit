a1=int(input("Digite o primeiro termo:  "))
r=int(input("Digite a razão:  "))
n=int(input("Digite a posição do termo que deseja encontrar:  "))
for c in range (1, n):
    an=a1+(c-1)*r
    print(f"TERMO {c}: {an} ")
soma=((a1+an)*n)/2
print(f"A soma dos termos é {soma}")

