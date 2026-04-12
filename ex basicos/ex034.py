
inventario=[]
while True:
    
    inventario.append(str(input("Digite o item que deseja adicionar: ")))
    print("-"*30)
    print("\033[7;36;40m          INVENTÁRIO          \033[m")
    print("-"*30)
    for nome in inventario:
        print(f"{nome}")
    resp=str(input("Deseja adicionar mais algo? [S/N]: ")).upper()
    if resp=="N":
        break


