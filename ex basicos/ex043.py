jogador=dict()
partidas=list()
time=list()
while True:
    jogador.clear()
    jogador['nome']=input("Nome do jogador: ")
    tot=int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantidade gols na partida {c+1}: ")))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input("Deseja continuar[S/N]: ")).upper()[0]
        if resp in 'SN':
            break
        print("Resposta inválida! Somente S ou N")
    if resp=='N':
        break

print('-'*100)
print(f'{"No.":<9}{"Nome":<12}{"Total Gols":>19}')     
print("-"*100)

for i, a in enumerate(time):
    print(f'{i:<9}{a['nome']:<12}{a['total']:19.1f}')

print(time)
print('-'*30)
while True:
    resp1=int(input("Digite o número do jogador (999 para parar): "))
    if resp1==999:
        break
    elif resp1 >=len(time):
        print("ERRO! Não existe jogador com esse registro.")
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[resp1]["nome"]}:')
        for a, b in enumerate (time[resp1]['gols']):
            print(f'No jogo {a+1} fez {b} gols')
