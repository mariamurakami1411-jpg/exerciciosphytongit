pessoas= dict()
info=list()
puc=list()
cont=0
for c in range (0,5):
    pessoas['nome']=str(input("Nome: "))
    pessoas['idade']=int(input("Idade: "))
    pessoas['Curso']=str(input("Curso: ")).upper()
    pessoas['Faculdade']=str(input("Faculdade: ")).upper()
    info.append(pessoas.copy())
    if pessoas['Faculdade']=='PUC':
        puc.append(pessoas.copy())
        cont+=1

print(f"A quantidade de estudantes que estudam na PUC é de {cont}")
print(f"Os seguintes estudantes cursam na PUC: ")
for pessoa in puc:
    print(f"{pessoa['nome']} - {pessoa['Curso']}")
