from rich import print
from rich.table import Table
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
        tabela=Table(title='Tabela de Preços')
        tabela.add_column('Nome')
        tabela.add_column('Preço')
        for linha in linhas:
            if linha.strip()=='':
                continue
            dado=linha.strip().split(';')
            tabela.add_row(f"{dado[0]}", f"{dado[1]}Kr")
        print(tabela)
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

def comprar(arq):
    try:
        a=open(arq, 'rt')
    except:
        print('Não foi possível abrir o arquivo.')
    else:
        nome=input('Digite o nome do produto que deseja comprar').upper()
        linhas=a.readlines()
        novas_linhas=[]
        for linha in linhas:
            if linha.strip()=='':
                continue
            if nome not in linha.upper():
                novas_linhas.append(linha)
        with open(arq, 'wt') as a:
            a.writelines(novas_linhas)
        print('Produto comprado/removido com sucesso!')
                






