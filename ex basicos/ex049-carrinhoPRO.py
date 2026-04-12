
# SISTEMA DE CARRINHO DE COMPRAS APRIMORADO
from time import sleep
produtos=[
    {'Nome': 'Processador', 'Preço': 1399.99},
    {'Nome': 'Placa Mãe', 'Preço': 749.99},
    {'Nome':'Memória RAM', 'Preço': 899.99 },
    {'Nome':'Placa de Vídeo', 'Preço': 2499.99},
    {'Nome':'Memória SSD', 'Preço': 749.99},
    {'Nome':'Cooler', 'Preço': 249.99},
    {'Nome':'Fonte', 'Preço': 439.99},
    {'Nome':'Fone de Ouvido', 'Preço': 199.99},
    {'Nome':'Teclado', 'Preço': 149.99},
    {'Nome':'Mouse', 'Preço': 99.99},
    {'Nome':'Monitor', 'Preço': 1299.99},
    {'Nome':'Gabinete', 'Preço': 499.99},
    {'Nome':'Microfone', 'Preço': 299.99},
    {'Nome':'Webcam', 'Preço': 199.99},
    {'Nome':'Headset', 'Preço': 399.99},
    {'Nome':'Mousepad', 'Preço': 49.99},
    {'Nome':'Cadeira Gamer', 'Preço': 899.99},
    {'Nome':'Extensão USB', 'Preço': 29.99},
    {'Nome':'Hub USB', 'Preço': 59.99}
]

carrinho= []

#Função para cadastrar produto
def cadastrar_prod():
    nome=(input('Escreva o nome do produto: '))
    preco=float(input("Escreva o preço do produto: "))
    produto= {
        'Nome': nome,
        'Preço': preco
    }
    produtos.append(produto)
    print('Produto cadastrado com sucesso!')


# Função para mostrar lista de produtos:
def listagem():
    print('-'*48)
    print('            PRODUTOS')
    print('-'*48)
    maior_nome=max(len(a['Nome']) for a in produtos)
    for i, u in enumerate(produtos):
        print(f"{i+1:<5}  {u['Nome']:<{maior_nome}}{'R$':>18} {u['Preço']}")
    print()


#Buscar produto
def escolha_prod():
    listagem()
    while True:
        while True:
            escolha=int(input('Escolha o número do produto: '))-1
            if escolha < len(produtos):
                print()
                print(f"{produtos[escolha]['Nome']:<20} R${produtos[escolha]['Preço']:>8.2f}")
                print()
                break
            print("ERRO! Produto inválido. ")
        while True:
            confirm=input("Voce quer adicionar produto ao carrinho [S/N]: ").upper()
            if confirm in 'SN':
                break
            print("Opção inválida! ", end='')
        if confirm=='S':
            carrinho.append(produtos[escolha])
            print('Processando...')
            sleep(1)
            print("Produto adicionado ao carrinho!")
        while True:
            resp=input("Voce deseja adicionar um outro item ao carrinho [S/N]: ").upper()
            if resp in 'SN':
                break
            print("Opção inválida! ", end='')
        if resp=='N':
            break
    
    
#Função para ver carrinho
def ver_carrinho():
    total=0
    if not carrinho:
        print("Carrinho vazio.")
        return
    print('-'*40)
    print(f'           CARRINHO')
    print('-'*40)
    maior_nome=max(len(a['Nome']) for a in carrinho)
    for item in carrinho:
        total+=item['Preço']
        
        print(f"{item['Nome']:<{maior_nome}}{'R$':>15} {item['Preço']}")
    print('-'*40)
    print(F'Total de itens: {len(carrinho):>17}')
    print(f"{'Total':<17}{'R$':>12} {total:.2f} ")
    print('-'*40)
    sleep(3)
    
#Função remover item
def remover_carrinho():

    if not carrinho:
        print("Carrinho vazio.")
        return
    print('-'*40)
    print(f'           CARRINHO')
    print('-'*40)
    maior_nome=max(len(a['Nome']) for a in carrinho)
    for i, u in enumerate(carrinho):
        print(f"{i+1:<5}  {u['Nome']:<{maior_nome}}{'R$':>18} {u['Preço']}")
    print()
    while True:
        while True:
            escolha=int(input('Escolha o número do produto que deseja excluir (999 para SAIR): '))-1
            if escolha==999:
                break
            elif escolha < len(carrinho):
                break
            print("ERRO! Produto inválido.")
        if escolha==999:
            break
        else:
            print(f"{carrinho[escolha]['Nome']:<20} R{carrinho[escolha]['Preço']:>8.2f}")
        while True:
            confirm=input("Voce quer remover produto ao carrinho [S/N]: ").upper()
            if confirm in 'SN':
                break
            print("Opção inválida! ", end='')
        if confirm=='S':
            item_removido=carrinho.pop(escolha)
            print('Processando...')
            sleep(1)
            print("Produto removido do carrinho!")
        while True:
            resp=input("Voce deseja remover um outro item ao carrinho [S/N]: ").upper()
            if resp in 'SN':
                break
            print("Opção inválida!", end='')
        if resp=='N':
            break

# Menu
print('-'*45)
print('          BEM-VINDO A KABUMM')
print('-'*45)

while True:
    sleep(1)
    print( '======= LOJA ======= ')
    print("Aperte [1] para cadastrar produto")
    print("Aperte [2] para ver a lista de produtos")
    print('Aperte [3] para adicionar um produto no carrinho')
    print('Aperte [4] para remover um produto do carrinho')
    print('Aperte [5] para ver o carrinho')
    print('Aperte [6] para Finalizar Compra')
    opcao=int(input("Escolha uma opção:"))
    if opcao==1:
        cadastrar_prod()
    elif opcao==2:
        listagem()
    elif opcao==3:
        escolha_prod()
    elif opcao==4:
        remover_carrinho()
    elif opcao==5:
        ver_carrinho()
    elif opcao==6:
        print('Processando compra...')
        sleep(2)
        print("Tudo certo!")
        sleep(1)
        print("Obrigada pela compra!")
        break
    else: 
        print("Opção inválida")
        
    