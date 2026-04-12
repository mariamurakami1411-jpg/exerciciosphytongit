# Programa de Votação Candidato Favorito
from time import sleep

print("-"*35)
print('    ELIÇÕES 2026 PARA PRESIDENTE')
print('-'*35)
resultado=list()
def porc(a,b):
    porcentagem=(a/b)*100
def votar():
    
    cont= cont1= cont2= cont3= cont4= cont0= 0   
    while True:
        print('-'*25)
        print(f"PESSOA {cont+1}")
        print('-'*25)
        print("Candidatos:")
        sleep(1)
        print('[ 12 ] Veronica Soneto')
        print('[ 26 ] Ricardo Nunes da Silva')
        print('[ 88 ] Katia Guimaraes')
        print('[ 45 ] Fernando Gomes')
        print('[ 0 ] Nulo')
        sleep(2)
        cont+=1
        while True:
            voto=int(input("Aperte o número correspondente ao candidato do seu voto: "))
            if voto==12:
                cont1+=1
                
                break
            if voto==26:
                cont2+=1
                
                break
            if voto==88:
                cont3+=1
                
                break
            if voto==45:
                cont4+=1
                
                break
            if voto==0:
                cont0+=1
                
                break
            print("Número inválido!")
        
        sleep(1)
        print("Obrigado pelo seu voto!")
        while True:
            pessoa=str(input('Voce deseja adicionar mais votante [S/N]: ')).upper()
            if pessoa in 'SN':
                break
            print("Opção inválida.")
        if pessoa=='N':
                print("Saindo...")
                break
    print(f'Total votos para Veronica: {cont1}')
    print(f'Total de votos para Ricardo: {cont2}')
    print(f'Total de votos para Katia: {cont3}')
    print(f'Total de votos para Fernando: {cont4}')
    print(f'Total de não votantes: {cont0}')


votar()
