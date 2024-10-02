n = input('Digite um número: ')
if not n.isdigit():
    print('ERRO. Número inválido.')
else:
    n = int(n)
    print(f'O número {n} é múltiplo de 2?', end=' ')
    if n % 2 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 3?', end=' ')
    if n % 3 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 4?', end=' ')
    if n % 4 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 5?', end=' ')
    if n % 5 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 6?', end=' ')
    if n % 6 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 7?', end=' ')
    if n % 7 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 8?', end=' ')
    if n % 8 == 0:
        print('Sim')
    else:
        print('Não')
    print(f'O número {n} é múltiplo de 9?', end=' ')
    if n % 9 == 0:
        print('Sim')
    else:
        print('Não')
