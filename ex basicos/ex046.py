tot=list()

def adc(lista):
    while True:
        num=int(input("Escreva um número: "))
        lista.append(num)

        while True:
            resp=input('Quer continuar [S/N]: ').upper()
            if resp in 'SN':
                break
            print("Opção inválida! Digite apenas S ou N")
        if resp=='N':
            break
       


def somaPar(lista):
    soma=0
    for v in lista:
        if v % 2== 0:
            soma+=v
    print(soma)

adc(tot)
somaPar(tot)

