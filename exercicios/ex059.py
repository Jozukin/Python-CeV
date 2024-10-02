op = 4
while op == 4:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))
    print('''Opções disponíveis para 2 números:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Corrigir Valores
    [ 5 ] Sair''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        s = n1 + n2
        print(f'O valor da soma entre {n1} e {n2} é igual a {s}')
    elif op == 2:
        m = n1 * n2
        print(f'O valor do produto entre {n1} e {n2} é igual a {m}')
    elif op == 3:
        nlist = [n1, n2]
        print(f'O maior valor entre {n1} e {n2} é {max(nlist)}')
    elif op == 4:
        print('Reiniciando o programa')
    elif op == 5:
        print('Encerrando o programa')
    else:
        print('Opção inválida, encerrando o programa')
