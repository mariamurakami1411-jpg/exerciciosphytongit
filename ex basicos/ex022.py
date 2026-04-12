from random import randint
jogadas=("Pedra" ," Papel" , "Tesoura")
computador=randint(0, 2)
print("Suas opções:  "
     " [0] PEDRA"
     " [1] PAPEL"
     " [2] TESOURA")
jogador=int(input("Qual a sua jogada:"))
if jogador==0 or jogador==1 or jogador==2:
    print("-="*11)
    print(f"Computador jogou {jogadas[computador]}")
    print(f"Jogador jogou {jogadas[jogador]}")
    print("-="*11)
    if computador==0 and jogador==2 or computador==2 and jogador==1 or computador==1 and jogador==0:
        print("Jogador perdeu! Computador venceu")
    else:
        print("Jogador venceu! Computador perdeu")
else:
    print("Opção inválida.")