print("\033[1;31;40mConversor de  Bases Numéricas\033[m")
num=int(input("Digite um número inteiro:"))
print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO")
print("[1] converter para OCTAL")
print("[1] converter para HEXADECIMAL")
opcao=int(input("Qual sua opção?:  "))
if opcao==1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)}")
elif opcao==2:
    print(f"{num} convertido para OCTAL é {oct(num)}")
elif opcao==3:
    print(f"{num} convertido para HEXADECIMAL é {hex(num)}")
else:
    print("Opção inválida")