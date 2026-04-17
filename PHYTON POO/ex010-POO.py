
class Aluno:
    contAluno=0
    contNota=0

    def __init__(self, nome, nota):
        self.nome=nome
        self.nota=nota
        Aluno.contAluno+=1
        Aluno.contNota += nota

    def info(self):
        return f"{self.name}: Nota {self.nota}"
    
    @classmethod
    def total_alunos(cls):
        return f"Total de alunos: {cls.contAluno}"
    
    @classmethod
    def nota(cls):
        if cls.contAluno ==0:
            return 0
        else:
            return f"Média das notas da turma: {cls.contNota / cls.contAluno:.2f}" 
    

aluno1 = Aluno("Ana", 8)
aluno2= Aluno("Herique", 6.5)
aluno3= Aluno('Julia', 9)
print(Aluno.total_alunos())
print(Aluno.nota())
    




