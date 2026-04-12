
invent=[]

monstro1=[
    'Garras de Besta',
    'Couro de Criatura',
    'Sangue Negro'
]
monstro2=[
    'Couro Mágico',
    'Núcleo Elemental',
    'Sangue Elemental'
]
monstro3=[
    'Essencia de Sombra',
    'Cinzas de Esqueleto',
    'Sangue Negro'
]

while True:
    escolha=int(input("Escolha um número de 1 a 3: "))
    if escolha==1:
        print("Parabéns!Voce ganhou os seguintes itens:")
        for nome in monstro1:
            print(f"- {nome}")
            invent.append(nome),
        break
    elif escolha==2:
        print("Parabéns!Voce ganhou os seguintes itens:")
        for nome in monstro2:
            print(
                    f"- {nome}"
                 )
            invent.append(nome),
        break
    elif escolha==3:
        print("Parabéns!Voce ganhou os seguintes itens:")
        for nome in monstro3:
            print(
                 f"- {nome}"
            )
            invent.append(monstro3),
        break
    else:
            print("Opção inválida")

escolha=(input("Deseja adicionar esses itens ao seu inventário [S/N]: ")).upper()
if escolha=="S":
    print("-"*30)
    print("INVENTÁRIO")
    print("-"*30)
    for nome in invent:
        print(f"{nome}")
    

    