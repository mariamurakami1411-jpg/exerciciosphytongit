dados=list()
pessoas=list()
while True:
    dados.append(str(input("Digite o nome: "))),
    dados.append(int(input("Digite a idade: "))),
    dados.append(float(input("Digite a altura em metros: "))),
    dados.append(float(input("Digite o peso em kg: ")))
    pessoas.append(dados[:])
    dados.clear()
    resp=input("Quer continuar[S/N]: ").upper()
    if resp=="N":
        break

    
    
for nome, idade, altura, peso in pessoas:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")
    print(f"Peso: {peso}")
    print("-"*15)
