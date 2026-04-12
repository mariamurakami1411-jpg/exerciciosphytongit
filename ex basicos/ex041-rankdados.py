# Fazendo um dado d20 de iniciativa
from random import randint
from time import sleep
from operator import itemgetter
jogadores=[]
pericias=[]
ranking=list()
jogo=list()
num=int(input("Quantos jogadores são: "))
for i in range (0, num):
   print('-'*15)
   print (f'JOGADOR {i+1}')
   print('-'*15)
   jogadores.append(str(input('Nome:')))
   jogadores.append(int(input("Iniciativa: ")))
   pericias.append(jogadores[:])
   jogadores.clear()
num1=int(input("Quantos Monstros são: "))
for a in range (0, num1):
   jogadores.append((f'Monstro {a+1}'))
   print(f"Monstro{a+1}")
   jogadores.append(int(input("Iniciativa: ")))
   pericias.append(jogadores[:])
   jogadores.clear()

print('Dados rodados: ')
for nome, pericia in pericias:
    d20= randint(1,20)
    dado=d20+pericia
    jogo.append(nome)
    jogo.append(dado)
    ranking.append(jogo[:])
    jogo.clear()

    print('-'*15)
    print(f'{nome}:')
    print(f'{dado} <- {d20} + {pericia}')

    
    sleep(1)
ranking.sort(key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
   print(f'{i+1} lugar: {v[0]} ({v[1]})')
   sleep(1)

