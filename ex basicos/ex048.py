def fatorial(f, show=False):
    tot=1
    for c in range (f, 0, -1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        tot=tot*c

   
    return tot
num=int(input("Digite um número: "))

while True:
    resp=input("Deseja ver a multiplicação do fatorial por inteiro [S/N]: ").upper()
    if resp in 'SN':
        break
    print('Opção inválida, Responda somente S ou N. ')
if resp=='S':
    n=True
if resp=='N':
    n=False
print(f'O fatorial de {num} é:')
print(fatorial(num, n))

