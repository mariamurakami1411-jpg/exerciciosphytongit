from rich import print
from time import sleep

class Funcionario():
    # Método Construtor
    def __init__(self):
        # Atributos de Instancia
        
        self.nome=''
        self.ano=0
        self.salario=3000
        
    
    
    # Métodos de Instancia
    def receber_dados(self):
        self.nome=input('Nome: ').strip()
        self.ano=int(input('Tempo na empresa( em anos): '))
        self.salario=int(input('Digite seu salario: '))
        return self.nome, self.ano, self.salario
    
    def calcular_bonus(self):

        if self.ano <1:
            bonus=1500
        elif self.ano <3:
            bonus=3500
        elif self.ano <6:
            bonus=6000
        else:
            bonus=9000

        
    
        return bonus
    

    def __str__(self):
        return f"{self.nome} tem salário igual a {self.salario}"

func1=Funcionario()
func1.receber_dados()
bonus=func1.calcular_bonus()
print(func1)
print(f'O bonus anual é de {bonus}')
        
    
    