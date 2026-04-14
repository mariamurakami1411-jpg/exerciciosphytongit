from datetime import datetime
from rich import print

class Tabela:
    def __init__(self,nome):
        self.nome=nome
        self.tarefas=[]

    def add(self,descr):
        self.tarefas.append(Tarefa(descr))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.status]
    
    def procurar(self, descr):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descr==descr][0]
    
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descr):
        # Atributos:
        self.descr=descr
        self.status=False
        self.duedate=datetime.today()
    
    def concluir(self):
        self.status=True
    
    def __str__(self):
        return self.descr + ('(Concluída)' if self.status else '')
    
def main():
    lista=Tabela('Tarefas de Casa')
    lista.add('Passar roupa')
    lista.add('Estudar programação')
    lista.add('Lavar louça')
    print(lista)

    lista.procurar('Lavar louça').concluir()
    for tarefa in lista.tarefas:
        print(f'- {tarefa}')
    print(lista)

if __name__=='__main__':
    main()



