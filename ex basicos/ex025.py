from datetime import date
atual=date.today().year
countM=0
countF=0
resp= "S"
count= 1
print("-_" *15)
print("\033[1;36;47mLISTA DE PESSOAS PARA ALISTAMENTO MILITAR\033[m")
print("-_" *15)
while resp == "S":
    print(f"------PESSOA {count}-------")
    nome=str(input("Digite o nome: ")).upper()
    nasc=int(input("Digite o ano de nascimento: "))
    sexo=str(input("Digite o sexo (M ou F):")).upper()
    if sexo!="M" and sexo!="F":
        print("Opção inválida!")
        sexo=str(input("Digite o sexo (M ou F):")).upper()
    pcd=str(input("Voce possui alguma deficiencia?(S/N): ")).upper()
    if pcd!="S" and pcd!="N":
        print("Opção inválida!")
        pcd=str(input("Voce possui alguma deficiencia?(S/N): ")).upper()
    idade= atual - nasc
    if sexo== "M" and idade >=18 and pcd=="N":
        countM=countM + 1
    elif sexo=="F" and idade >=18 and pcd=="N":
        resp2=str(input("Deseja participar do alistamento?(S/N):")).upper() 
        if resp2=="S":
            countF=countF +1
        elif resp2!="S" and resp2!="N":
            print("Opção inválida!")
    resp=str(input("Deseja adicionar mais participantes? (S ou N): ")).upper()
    if resp!="S" and resp!="N":
        print("Opção inválida!")
        resp=str(input("Deseja adicionar mais participantes? (S ou N): ")).upper()
    count=count +1
print(f"O total de homens maiores de 18 anos aptos para o alistamento é de {countM} ")
print(f"O total de mulheres maiores de 18 anos que desejam participar do alistamento militar é de {countF}")

