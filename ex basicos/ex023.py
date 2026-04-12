dados_dolar=[
    5.12, 5.15, 5.18, 5.10, 5.08, 
    5.20, 5.25, 5.30, 5.28, 5.22, 
    5.18, 5.16, 5.19, 5.23, 5.27, 
    5.30, 5.35, 5.40, 5.38, 5.32,
    5.28, 5.25, 5.22, 5.20, 5.18, 
    5.15, 5.12, 5.10, 5.08, 5.05
]
tempo=int(input("Digite o período de dias que deseja analisar (máx 30):  "))
#Validação
if tempo>len(dados_dolar) or tempo <= 1:
    print("Tempo inválido")
else:   
    alta= 0
    queda= 0
    soma=0
    i=len(dados_dolar)-tempo
for c in range (i, len(dados_dolar)):
    if dados_dolar[c] > dados_dolar[c-1]:
        alta=alta+1
    else:
        queda=queda+1

    soma=soma+dados_dolar[c]

media=soma/tempo
print(f"Média do dólar:{media:.3f}")

#Funções
def mostrar_alta():
    print(f"Altas:{alta}")
def analisar():
    print("O mercado está em alta!")
def mostrar_baixa():
    print(f"Baixas: {queda}")
def analisar2():
    print("O mercado está em baixa!")


mostrar_alta()
mostrar_baixa()
if alta > queda:
    analisar()
else:
    analisar2()
