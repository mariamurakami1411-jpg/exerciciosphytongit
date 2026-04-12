#Declaração de Classe
class Jogador:
    def __init__(self, n='Desconhecido', i='desconhecido'): #método Construtor
        # Atributos de Instancia
        self.nome= n
        self.idade= i

    # Métodos de Instancia
    def aniversario(self):
        self.idade+=1
    
    def __str__(self):
        return f"{self.nome} é Jogador(a) e tem {self.idade} anos de idade"


#Declaração de OBjetos
jg= Jogador('Maria', 18)
jg.aniversario()
print(jg)

jg2= Jogador('Joao', 21)
print(jg2)

jg3=Jogador()
print(jg3)