from random import randint
from time import sleep

# Simulador RPG
print("\033[1;35;47m----------SIMULADOR LUTA RPG----------\033[m")
print(" ")
# Dados personagem
print("-=-=-=-=-=-PERSONAGEM-=-=-=-=-=-=-")
nomeper=str(input("Escreva o nome do personagem:"))
vidabase1=int(input("Vida inicial: "))
danobase1=int(input("Dano base: "))
ataque1=int(input("Perícia ATAQUE: "))
defesa1=int(input("Perícia DEFESA: "))
print("-="*15)

# Dados inimigo
print("-=-=-=-=-=-=-INIMIGO-=-=-=-=-=-=-")
nomeinimg=("Inimigo")
vidabase2=int(input("Vida inicial:"))
danobase2=int(input("Dano base: "))
ataque2=int(input("Perícia ATAQUE: "))
defesa2=int(input("Perícia DEFESA: "))
print("-="*15)
vidajog=vidabase1
vidainimig=vidabase2
count=1

# Turnos
while vidajog > 0 and vidainimig > 0:
    print(f"\033[1;36;40m----RODADA {count}----\033[m")
# Turno do Jogador
    print(f"\033[7;37mTurno de {nomeper}\033[m")
    print("--AÇÃO 1--")
    print("Pressiona [1] para ATACAR:")
    acao=int(input(" "))
    jogd20= randint(1,20)
    inimigd20= randint(1,20)
    if acao==1:
        turnojog=jogd20+ataque1
        definimig=inimigd20+defesa2
        print(f"Ataque {nomeper}: {turnojog} <-[{jogd20}] 1d20+{ataque1}")
        sleep(1)
        print(f"Defesa Inimigo: {definimig} <- [{inimigd20}] 1d20+{defesa2}")
        sleep(2)

        if turnojog >= definimig:
            if jogd20 == 20:
                vidainimig=vidainimig-(danobase1*2)
            else:
                vidainimig=vidainimig-danobase1
            if vidainimig <=0:
                break
            print("\033[1;33mVoce acertou seu ataque!\033[m")
                
        else:
            print("\033[1;35mVoce errou o seu ataque\033[m!")
        sleep(1)
        print(f"Vida atual de {nomeper}: {vidajog}")
        print(f"Vida atual do Inimigo: {vidainimig}")

        

    else:
        print("Opção inválida!")
        while acao!=1:
            print("Opção inválida!")
            print("Pressiona [1] para ATACAR:")
            acao=int(input(" "))

    print("--AÇÃO 2--")

    print("Escolha uma das opções:")
    print("[ 1 ] ATACAR")
    print("[ 2 ] FUGIR")
    acao=int(input(" "))
    
    if acao==1:
        jogd20= randint(1,20)
        inimigd20=randint(1,20)
        turnojog=jogd20+ataque1
        definimig=inimigd20+defesa2
        print(f"Ataque {nomeper}: {turnojog} <-[{jogd20}] 1d20+{ataque1}")
        sleep(1)
        print(f"Defesa Inimigo: {definimig} <- [{inimigd20}] 1d20+{defesa2}")
        if jogd20 == 20:
            vidainimig=vidainimig-(danobase1*2)
        if turnojog >= definimig:   
            vidainimig=vidainimig-danobase1
            print("\033[1;33mVoce acertou seu ataque!\033[m")
        else:
            print("\033[1;35mVoce errou o seu ataque\033[m!")
        sleep(2)
        print(f"Vida atual de {nomeper}: {vidajog}")
        print(f"Vida atual do Inimigo: {vidainimig}")
    elif acao==2:
        print("Voce fugiu! Covarde!")
        break
    else:
        print("Opção inválida!")
       
        
        
    go=int(input("Pressione [ 1 ] para CONTINUAR: "))
    while go!=1:
        print("Opção inválida!")
        go=int(input("Pressione [ 1 ] para CONTINUAR: "))
    
    print("--"*8)

#Turno do Inimigo
    print(f"\033[7;37mTurno do Inimigo\033[m")
    print("--AÇÃO 1--")
    jogd20= randint(1,20)
    inimigd20=randint(1,20)
    ataqinimig=inimigd20+ataque2
    defjog=jogd20+defesa1
    print(f"Ataque Inimigo: {ataqinimig} <- [{jogd20}] 1d20+{ataque2}")
    sleep(1)
    print(f"Defesa {nomeper}: {defjog} <-[{inimigd20}] 1d20+{defesa1}")
    sleep(2)
    if inimigd20 ==20:
        vidajog=vidajog-(danobase2*2)
    if ataqinimig >= defjog:
        
        vidajog=vidajog-danobase2
        if vidajog <=0:
            break
        print("\033[1;31mInimigo acertou o ataque!\033[m")
       
    else:
        print("\033[1;32mInimigo errou o ataque!\033[m")
   
    print(f"Vida atual de {nomeper}: {vidajog}")
    print(f"Vida atual do Inimigo: {vidainimig}")
    

    go=int(input("Pressione [ 1 ] para CONTINUAR: "))
    while go!=1:
        print("Opção inválida!")
        go=int(input("Pressione [ 1 ] para CONTINUAR: "))
    
    print("--AÇÃO 2--")
    jogd20= randint(1,20)
    inimigd20=randint(1,20)
    ataqinimig=inimigd20+ataque2
    defjog=jogd20+defesa1
    print(f"Ataque Inimigo: {ataqinimig} <-[{jogd20}] 1d20+{ataque2}")
    sleep(1)
    print(f"Defesa {nomeper}: {defjog} <- [{inimigd20}] 1d20+{defesa1}")
    sleep(2)
    if inimigd20 == 20:
         vidajog=vidajog-(danobase2*2)
    elif ataqinimig >= defjog:
        vidajog=vidajog-danobase2
        print("\033[1;31mInimigo acertou o ataque!\033[m")
    else:
      print("\033[1;32mInimigo errou o ataque!\033[m")
    print(f"Vida atual de {nomeper}: {vidajog}")
    print(f"Vida atual do Inimigo: {vidainimig}")
    count=count+1

sleep(1)
if vidajog <=0:
    print("\033[1;31mVoce falhou. Inimigo venceu.\033[m")
elif vidainimig <=0:
    print("\033[1;32mParabéns! Voce derrotou o inimigo!\033[m")
else:
    print("Voce é uma vergonha...")