salario=int(input("Qual o seu salário?:"))
if salario <= 2000:
    novosalario=salario+(salario*0.3)
if salario > 2000 and salario <= 4000:
    novosalario=salario+(salario*0.12)
if salario > 4000 and salario <=8000:
    novosalario=salario+(salario*0.075)
if salario > 8000:
    novosalario=salario+(salario*0.045)
print(f"O seu novo salário será de \033[1;31;40mR${novosalario}\033[m")