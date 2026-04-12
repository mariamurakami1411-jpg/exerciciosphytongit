imovel=int(input("Olá! Quantos custa o imóvel?:"))
salario=int(input("Quanto é o seu salário?:"))
entrada=int(input("Informe o valor da entrada:"))
meses=int(input("Informe quantos meses pretende financiar: "))
prestacao=round((imovel-entrada)/meses, 2)
if prestacao <= (salario*0.3):
    print("Voce está dentro da faixa para realizar essa aquisição!")
    print(f"O valor da prestação será de \033[4;32mR${prestacao}\033[m")
else:
    print("Sua negociação não pode ser continuada pois seu salário não encaixa nas condições de prestação do imóvel.")
