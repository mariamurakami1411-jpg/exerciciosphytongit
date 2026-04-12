class Contabancaria:
    def __init__(self, id, nome, saldo=0):
        self.id=id
        self.titular=nome
        self.saldo=saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        self.saldo+=valor
        print(f'Depósito de R${valor} realizado')
        
        
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saque não autorizado. Saldo insuficiente')
        else:
            self.saldo-=valor
            print(f'Saque de R${valor} realizado.')

    


c1= Contabancaria(101, 'Maria Clara', 3000)
c1.depositar(500)
c1.sacar(1000)
print(c1)
