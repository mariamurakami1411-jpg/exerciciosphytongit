import os
os.chdir(r"C:\Users\55419\Desktop\Curso Phyton\exercicios phyton\PHYTON POO\ex004")


def arquivoExiste(nome):
    
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    
    try:
        a=open(nome, 'wt+')
        a.close()
    except:
        print('Houve um problema na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso!')

def lerAquivo(nome):
    
    try:
        a=open(nome, 'rt')
    except:
        print('Erro ao ler o aquivo.')
    else:
        print('PRODUTOS CADASTRADOS')
        linhas=a.readlines()
        maior_nome=0
        dados=[]
       
        for linha in linhas:
            if linha.strip()=='':
                continue
            dado=linha.strip().split(';')
            if len(dado)<2:
                continue
            dados.append(dado)

            if len(dado[0])>maior_nome:
                maior_nome=len(dado[0])

            maior_nome=max(maior_nome,11)
           
        print('-'*50)
        print(f'"{"No.":<9}{"Nome":<{maior_nome}}{"Preço":>9}')
        print("-"*50)
        for i, dado in enumerate(dados):
            print(f'{i+1:<9}{dado[0]:<{maior_nome}}{dado[1]:>8}K')
    
    finally:
        a.close()
       
def cadastrar(arq, nome='desconhecido', preco=0 ):
    try:
        a=open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{preco}\n')
        except:
            print('Houve um erro ao cadastrar os dados.')
        else:
            print(f'Novo registro cadastrado com sucesso!')
            a.close()