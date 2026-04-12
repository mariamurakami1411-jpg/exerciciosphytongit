print("\033[2;32;40m=====LOJA KABUM!=====\033[m") 
valor=float(input("Valor total: "))
parc2=(valor-(valor*0.07))
print("Escolha a forma de pagamento:")
print("\033[1;31m[ 1 ]\033[m a vista no Pix ou cartão débito (desconto 12%)")
print("\033[1;31m[ 2 ]\033[m 2x no cartão (desconto 7%)")
print("\033[1;31m[ 3 ]\033[m 3x ou mais no cartão (Juros de 7.5%)")
opcao=int(input("Qual opção deseja escolher?: "))
if opcao == 1:
    parc=1
    total=(valor-(valor*0.12))/parc
elif opcao== 2:
    parc=2
    total=parc2/parc
elif opcao== 3:
    parc=int(input("Digite o número parcelas que deseja realizar o pagamento:"))
    total=(valor+(valor*0.075))/parc
else:
    print("Opção inválida")
if opcao == 1 or opcao== 2:
    print(f"Obrigada pela compra! O valor total é de \033[1;35mR${total} em {parc} parcela(s) sem juros\033[m")
elif opcao ==3:
    print(f"Obrigada pela compra!O valor total será de \033[1;31mx{parc} parcelas\033[m de \033[1;35mR${total:.2f} com juros\033[m")

