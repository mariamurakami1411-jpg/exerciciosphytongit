from time import sleep
usuarios=list()
def cadastro():
    
    
    nome=input("Nome completo: ").upper()
    idade=input("Idade: ")
    curso=input("Curso: ").upper()
    
    usuario={
        'Nome': nome, 
        'Idade': idade, 
        'Curso': curso
    }
    usuarios.append(usuario.copy())
    print("Usuário cadastrado com sucesso!")
    print(usuarios)

def listagem():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    maior_nome=max(len(a['Nome']) for a in usuarios)
    maior_curso=max(len(u['Curso'])+3 for u in usuarios)
    print('LISTA DE USUÁRIOS:')
    print('-'*100)
    print(f'"{"No.":<9}{"Nome":<{maior_nome}}{"Idade":>9}{"Curso":>{maior_curso}}')
    print("-"*100)
    for i, a in enumerate(usuarios):
        print(f'{i+1:<9}{a['Nome']:<{maior_nome}}{a['Idade']:>8}{a['Curso']:>{maior_curso}}')

while True:
    print("Aperte [1] para cadastrar usuário")
    print("Aperte [2] para ver a lista de usuários")
    print("Aperte [3] para Sair")
    opcao=int(input("Escolha uma opção:"))
    if opcao==1:
        cadastro()
    elif opcao==2:
        listagem()
    elif opcao==3:
        print("Até logo!")
        break
    else: 
        print("Opção inválida")
        sleep(1)
    



