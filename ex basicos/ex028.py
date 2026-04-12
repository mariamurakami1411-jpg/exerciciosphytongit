from random import randint
v=0
while True:
    num=int(input("Digite um valor: "))
    comp= randint(0, 20)
    tot= num + comp
    tipo= ' '
    while tipo not in 'PAR''IMPAR''P''I':
        tipo=str(input("Par ou Ímpar?: ")).strip().upper()
    print(f"Voce jogou {num} e o Computador {comp}. Total= {tot}")
    if tipo=='P'or tipo=='PAR':
        if tot % 2 ==0:
            print("Parabéns!Voce GANHOU!")
            v+=1
        else:
            print("Voce PERDEU!")
            break
    elif tipo=='I'or tipo=='IMPAR':
        if tot % 2 ==1:
            print("Voce GANHOU!")
            v+=1
        else:
            print("Voce PERDEU!")
            break
    print('Vamos jogar novamente...')
print(f"GAME OVER! Voce venceu {v} vezes.")    
