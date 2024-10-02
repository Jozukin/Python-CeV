n = input('Digite um número: ')
if not n.isdigit():
    print('ERRO. Número inválido.')
else:
    n = int(n)
    if n % 2 == 0:
        print(f'O número {n} é par')
    else:
        print(f'O número {n} é ímpar')
