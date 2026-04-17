import moedas
import cor

def converter(p):
    p=int(input('Digite o valor em Krons: '))
    print(f'Saldo em {cor.vermelho()}Rubrens{cor.reset()}: \t{moedas.rubren(p)}')
    print(f'Saldo em {cor.ciano()}Neurobit{cor.reset()}: \t{moedas.neurobit(p)} ')
    print(f'Saldo em {cor.verde()}Lingyuan{cor.reset()}: \t{moedas.lingyuan(p)}')
    print(f'Saldo em {cor.azul()}Kuan{cor.reset()}: \t\t{moedas.kuan(p)}')
    print(f'Saldo em {cor.roxo()}Arkanium{cor.reset()}: \t{moedas.arkanium(p)}')
    print(f'Saldo em {cor.amarelo()}Aeris{cor.reset()}: \t{moedas.aeriscoin(p)}')


