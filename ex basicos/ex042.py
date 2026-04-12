from datetime import date

cadastro=dict()
cadastro['Nome']=str(input("Nome: "))
cadastro['Nasc']=int(input("Ano de Nascimento: "))
cadastro['Idade']= date.today().year - cadastro['Nasc']
cadastro['Contr']=int(input("Ano de Contratação: "))
cadastro['Salario']=float(input("Salário: R$"))

cadastro['Aposentadoria']= (cadastro['Idade']+(cadastro['Contr']+ 35)- date.today().year) 
print(cadastro)
