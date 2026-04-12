def address(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


address(Endereço='Rua Nao Sei 88', Cidade='São Paulo', Estado='SP', CEP='215486')

def correio(**kwargs):
    for i, u in kwargs.items():
        print(f'{i: {u}}')



nome=str(input('Nome: ')).upper()
sobrenome=str(input('Sobrenome: ')).upper()
endereço=str(input('Endereço: ')).upper()
número=int(input('No.: '))
bairro=str(input('Bairro: ')).upper()
cidade=str(input('Cidade: ')).upper()
estado=str(input('Estado: ')).upper()  
a={
    'Nome': nome,
    'Sobrenome': sobrenome,
    'Endereço': endereço,
    'No. ': número,
    'Bairro': bairro,
    'Cidade': cidade,
    'Estado': estado

    
}
correio(a)