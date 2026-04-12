nota1=float(input("Digite sua primeira nota:  "))
nota2=float(input("Digite sua segunda nota:  "))
nota3=float(input("Digite sua terceira nota:  "))
media=(nota1+nota2+nota3)/3
if media >= 7:
    print("PARABÉNS! Voce está APROVADO!")
elif media < 7 and media >=4:
    print("Voce está de RECUPERAÇÃO.")
else:
    print("Voce foi REPROVADO.")
