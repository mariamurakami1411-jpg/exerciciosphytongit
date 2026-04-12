print('='*30)
print('          BANCO DEV')
print('='*30)
print("Digite o valor do saque:")
valor=int(input('R$'))
total= valor
cedulas= 200, 100, 50, 20, 10, 5, 1
for ced in cedulas:
    totced= total//ced
    if totced > 0:
        print(f"O total foi de {totced} de R${ced}")
        total=total % ced
 

        

