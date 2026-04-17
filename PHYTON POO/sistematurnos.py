from random import randint
from time import sleep
from operator import itemgetter

class Jogador:
    def __init__(self,nome,hp):
        self.nome=nome
        self.hp=hp


class Iniciativa(Jogador):
    def __init(self, nome, pericia):
        super().__init__(nome)
        self.dado=pericia
    
    def rolar_dado(self):
        d20= randint(1,20)
        dado=d20+self.pericia
        print('-'*15)
        print(f'{self.nome}:')
        print(f'{dado} <- {d20} + {self.pericia}')
    
class Turnos(Iniciativa):
    def __init__(self, nome, pericia):
        super().__init__(nome,pericia )
        self.jogadores=[]

    def add(self):
        self.jogadores.append(Iniciativa(nome, pericia))
        


num=int(input("Quantos jogadores são: "))
for i in range (num):
    print('-'*15)
    print (f'JOGADOR {i+1}')
    print('-'*15)
    nome=str(input('Nome:'))
    pericia=int(input("Iniciativa: "))
    jogadores.append(Iniciativa(nome, pericia))
for j in jogadores:
    print(j)



