info=dict()
pessoas=list()
soma=0
while True:
    info['Nome']=str(input("Nome: "))
    info['Idade']=int(input("Idade: "))
    soma+=info['Idade']
    while True:
        info['Sexo']=str(input("Sexo: ")).upper()[0]
        if info['Sexo'] in'MF':
            break
        print('ERRO-- por favor, digite M ou F.')
    pessoas.append(info.copy())
    while True:
        resp=str(input("Deseja adicionar mais uma pessoas [S/N]: ")).upper()[0]
        if resp in 'SN':
            break 
        print('ERRO! Responda apenas S ou N')
    if resp=='N':
        break
    info.clear()
media=soma/len(pessoas)
print(f'Temos ao todo {len(pessoas)} cadastradas.')
print(f'A média de idades foi de {media:.1f} anos')
cont=0
for a, b, c in pessoas:
    if c >= media:
        cont=+1
print(f'Ao total temos {cont} pessoa(s) acima da média de idade.')
