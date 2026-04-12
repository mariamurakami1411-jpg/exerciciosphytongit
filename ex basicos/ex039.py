from random import randint
print('-='*15)
print("         MEGA-SENA")
print("-="*15)
l=[]
jogos=[]
jogo=[]
result=[]
count=0
tot=1

print('Escolha uma das opções:')
print(f'Aperte [1] para receber um jogo aleatório.')
print(f'Aperte [2] para escolher manualmente seus números.')
resp2=int(input(''))
if resp2==1:
    cont=0
    while True:
        num=randint(1,60)
        if num not in l:
            l.append(num)
            cont+=1
        if cont >=6:
            
            break
    l.sort()
    
elif resp2==2:
    for a in range (0,6):
        l.append(int(input(F"Digite o numero {a+1}: ")))

    
else:
    print("Opção Inválida.")

for b in range(0,6):
    jogo.append(randint(1,60))

for c in range(0,6):
    result=l[c]-jogo[c]
    if result==0:
        count+=1
print(f'Seu jogo: {l}')
print(f'Resultado: {jogo}')
if count==0 or count<=3:
    print("Voce nao ganhou nada! Boa sorte na próxima vez!")
if count==4:
    print("Parabéns! Voce ganhou 10 reais")
if count==5:
    print("Parabéns! Voce ganhou 500 reais")
if count==6:
    print("Parabéns! Voce ganhou 1 MILHAO DE REAIS!!")

