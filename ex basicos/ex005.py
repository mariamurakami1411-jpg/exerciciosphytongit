invi=int(input("Digite o valor do investimento: "))
mes=int(input("Digite a quantidade de meses: "))
cdi=14.65/100
taxam=(1+cdi)**(1/12)-1
invf=round(invi+((invi*taxam)*mes))
print(f"O rendimento bruto em {mes} será de {invf},00 reais")