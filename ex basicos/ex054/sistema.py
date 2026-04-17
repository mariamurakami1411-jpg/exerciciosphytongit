from arquivos.arquivo import *
from time import sleep
from rich import print

arq='cadastros.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    print("Aperte [1] para [bold yellow]cadastrar usuário[/]")
    print("Aperte [2] para ver a [bold green]lista de usuários[/]")
    print("Aperte [3] para [bold red]Sair[/]")
    opcao=int(input("Escolha uma opção:"))
    if opcao==1:
        print('-'*20)
        print('NOVO CADASTRO:')
        print('-'*20)
        nome=str(input('Nome: ')).upper()
        try:
            idade=int(input('Idade: '))
        except (ValueError, TypeError):
            print('ERRO. Por favor, digite um número inteiro válido')
        curso=str(input('Curso: ')).upper()
        cadastrar(arq, nome, idade, curso)
    elif opcao==2:
        lerAquivo(arq)
    elif opcao==3:
        print("Até logo!")
        break
    else: 
        print("Opção inválida")
        sleep(1)
    