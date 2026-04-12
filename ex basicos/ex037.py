print("-"*30)
print("      REGISTROS DE NOTAS")
print("-"*30)
registro= []
mai=0
nmai=''
nmen=''
men=0
c=0
resp="S"
while resp=="S":
    c+=1
    nome=input("Nome: ").upper()
    
    nota1=float(input("Nota 1: "))
    
    nota2=float(input("Nota 2:"))
    
    media=round((nota1+nota2)/2, 2)
    registro.append([nome, nota1, nota2, media])
    print(f"Média Final: {media}")
    
    resp=input("Deseja adicionar mais alunos [S/N]: ").upper()
    if resp=="N":
        break
    else:
        print("Opção Inválida!")
        resp=input("Deseja adicionar mais alunos [S/N]: ").upper()

maior_nome=max(len(a[0]) for a in registro)

print('-'*100)
print(f'{"No.":<9}{"Nome":<{maior_nome}}{"Nota 1":>19}{"Nota 2":>21}{"Média":>23}')
print("-"*100)

for i, a in enumerate(registro):
    print(f'{i:<9}{a[0]:<{maior_nome}}{a[1]:>15}{a[2]:>17}{a[3]:19.1f}')



