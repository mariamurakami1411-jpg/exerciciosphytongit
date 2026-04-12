from arquivo.arquivo import *
from time import sleep
from rich import print

arq='itens.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    print("Aperte [1] para [bold white]cadastrar item[/]")
    print("Aperte [2] para [bold white]ver a lista de itens[/]")
    print("Aperte [3] para [bold red]Sair[/]")
    opcao=int(input("Escolha uma opção:"))
    if opcao==1:
        print('-'*20)
        print('NOVO CADASTRO:')
        print('-'*20)
        nome=str(input('Nome: ')).upper()
        try:
            preco=int(input('Preço: '))
        except (ValueError, TypeError):
            print('ERRO. Por favor, digite um número inteiro válido')
        cadastrar(arq, nome, preco, )
    elif opcao==2:
        lerAquivo(arq)
        print()
    elif opcao==3:
        print("Até logo!:hand:")
        break
    else: 
        print("Opção inválida")
        sleep(1)