#Declaração de Classe
class Jogador:
    def __init__(self): #método Construtor
        # Atributos de Instancia
        self.nome=''
        self.idade=0

    # Métodos de Instancia
    def aniversario(self):
        self.idade+=1

    def mensagem(self):
        return f"{self.nome} é Jogador(a) e tem {self.idade} anos de idade"


#Declaração de OBjetos
jg= Jogador() # ()- Instanciação
jg.nome='Maria'
jg.idade=18 # Percebe-se que, atributos não possuem parenteses()
            # Atributos nao tem parenteses
            # Métodos tem parenteses
jg.aniversario()
print(jg.mensagem())

jg2= Jogador()
jg2.nome=input('Digite o nome do jogador: ')
jg.idade=int(input('Idade: '))

print(jg2.mensagem())