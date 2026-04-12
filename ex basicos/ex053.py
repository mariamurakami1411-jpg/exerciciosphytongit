try:
    n=int(input('Digite um valor: '))
except (ValueError, TypeError):
    print('ERRO. Por favor, digite um número inteiro válido')
else:
    try:
        s=int(input('Digite o divisor: '))
        div= n / s
    except (ValueError, TypeError):
        print('ERRO. Por favor, digite um número inteiro válido')
    except (ZeroDivisionError):
        print('Não é possível dividir este número por zero.')
    except (KeyboardInterrupt):
        print('O usuário preferiu não digitar esse número.')
    else:
        print(f'O resultado é digitado foi {div:.1f}')