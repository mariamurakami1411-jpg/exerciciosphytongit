def neurobit(kron):
    res=kron//5
    return res

def arkanium(kron):
    res=kron//100
    return res

def lingyuan(kron):
    res=kron//50
    return res

def kuan(kron):
    res=kron//2
    return res

def rubren(kron):
    res=kron//10
    return res

def aeriscoin(kron):
    res=kron/5000
    return res

def resumo(valor):
    
    
    print(f'Saldo em Rubrens: \t{rubren(valor)}')
    print(f'Saldo em Neurobit: \t{neurobit(valor)} ')
    print(f'Saldo em Lingyuan: \t{lingyuan(valor)}')
    print(f'Saldo em Kuan: \t\t{kuan(valor)}')
    print(f'Saldo em Arkanium: \t{arkanium(valor)}')
    print(f'Saldo em Aeris: \t{aeriscoin(valor)}')

def carteira(lista):
    print()
    print('-'*35)
    print('CARTEIRA DE MOEDAS')
    print('-'*35)
    print(f'{'Saldo em Krons':<6} \t\t{'K$'}{sum(lista)}')


