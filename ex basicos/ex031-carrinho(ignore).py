produtos= (
    ("Processador", 1399.99),
    ("Placa-Mãe", 749.99),
    ("Memória RAM", 899.99 ),
    ("Placa de Vídeo", 2499.99),
    ("Memória SSD", 749.99),
    ("Cooler", 249.99),
    ("Fonte", 439.99),
    ("Fone de Ouvido", 199.99),
    ("Teclado", 149.99),
    ("Mouse", 99.99),
    ("Monitor", 1299.99),
    ("Gabinete", 499.99),
    ("Microfone", 299.99),
    ("Webcam", 199.99),
    ("Headset", 399.99),
    ("Mousepad", 49.99),
    ("Cadeira Gamer", 899.99),
    ("Extensão USB", 29.99),
    ("Hub USB", 59.99)
    
)
print('-'*33)
print('        LOJAS DEV')
print('-'*33)
c= 0
total= 0
bnome=''
cnome=''
carrinho= []
print("Olá! Seja Muito bem-vindo!")
resp1="S"
answer =(input("Voce deseja ver a Lista de Produtos [S/N]:")).upper()
if answer=="S":
    print('-'*42)
    print('            PRODUTOS')
    print('-'*42)
    for nome1,preco1 in produtos:
        print(f"{nome1:<20} R${preco1:>18}")
        answer="N"
if not answer=="S":
    while resp1=="S":
        prod=str(input("Qual produto deseja procurar: ")).upper()
        encontrado= []
        for nome, preco in produtos:
            if nome.upper() in prod:
                encontrado.append(prod)
                print('Produto encontrado!')
                for i, a, b in enumerate(encontrado):
                    print(f"{i}.  {a:<20} R${b:>8.2f}")
                while True:
                    resp1=int(input("Digite o número do produto (999 para parar): "))
                    if resp1==999:
                        break
                    elif resp1 >=len(encontrado):
                        print("ERRO! Não existe produto com esse registro.")
                    else:
                        resp=str(input("Voce deseja adicionar este item em seu carrinho [S/N]: ")).upper()
                        if resp=="S":
                            carrinho.append((encontrado[resp1-1]))
                print('-'*33)
                print('CARRINHO')
                for nome, preco in carrinho:
                    print(f"{nome:<20} R${preco:>8}")
                    total= sum(preco for nome, preco in carrinho)
                print("")
                print(f"{'Total:':<20} R${total:>8.2f}")
                c+=1
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
                
                if not encontrado:
                    print("Produto não encontrado.")
            print('-'*33)
            resp1=str(input("Voce deseja continuar procurando [S/N]: ")).upper()
            if resp1=='N':
                break
        

        
    print(f"O total de itens foi {c}")
    print(f"O valor total da compra é R${total:.2f}")
    if c>2:
        print(f"O item mais caro da lista foi {cnome}, custando R${caro}")
        print(f"O item mais barato da lista foi {bnome}, custando R${barato}")
        



