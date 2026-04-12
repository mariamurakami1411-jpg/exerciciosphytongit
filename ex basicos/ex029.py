print('-='*12)
print("      lOJA KABUMM!")
print('-='*12)
resp= "S"
c= 0
total= 0
bnome=''
cnome=''
while resp=="S" or resp=="SIM":
    c+=1
    nome=str(input('Nome do Produto: '))
    preco=float(input('Preço: R$'))
    total= total + preco
    resp=str(input('Quer continuar? [SIM/NAO]: ')).strip().upper()
    
    if c==1:
        barato=preco
        bnome= nome
    elif c==2:
        if preco < barato:
            barato=preco
            bnome=nome
        else:
            caro=preco
            cnome= nome
    else:
        if preco < barato:
            barato=preco
            bnome=nome
        if preco > caro:
            caro=preco
            cnome=nome
    
print(f"O total de itens foi {c}")
print(f"O valor total da compra é R${total:.2f}")
if c>2:
    print(f"O item mais caro da lista foi {cnome}, custando R${caro}")
    print(f"O item mais barato da lista foi {bnome}, custando R${barato}")



