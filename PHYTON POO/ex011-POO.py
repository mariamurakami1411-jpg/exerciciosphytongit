


class Banco:
    def __init__(self):
        self.nome=''
        self.senha=''
        self.saldo=0
        self.lista=[]

    


    def __str__(self):
        return f'{self.lista}'

    
class Usuario(Banco):
    def cadastrar(self):
        self.nome=input('Nome: ')
        self.senha=input('Senha: ')
        self.saldo=float(input('Saldo: '))
        cadastro= {
            'Nome': self.nome,
            'Senha': self.senha,
            'Saldo': self.saldo
        }
        self.lista.append(cadastro)

    def login(self):
        self.nome=input('Nome: ')
        self.senha=input('Senha: ')
        for n in self.lista:
            if self.nome in self.lista:
                if self.senha in self.lista:
                    print(f'{self.lista[n]}')

pessoa1=Usuario()
pessoa1.cadastrar()
print(pessoa1)
pessoa1.login()


        



