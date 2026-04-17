from uteis import moedas
saldo=[]


while True:
    moedas.carteira(saldo)
    moedas.resumo(sum(saldo))
    print(' ')
    while True:
        resp=input('Deseja adicionar Krons a sua conta [S/N]: ').upper()
        if resp in 'SN':
            break
        print('Resposta inválida!')
    if resp=='S':
        p=int(input('Digite o valor em Krons: '))
        saldo.append(p)

    if resp=='N':
        break
   

       
       
        



   
