n = input('Digite um número que deseja converter: ')
print('1 = binário\n2 = octal\n3 = hexadecimal')
op = input('Qual conversão deseja fazer? ')
if n.isdigit() and op.isdigit():
    n = int(n)
    op = int(op)
    if op == 1:
        print(f'O número {n} convertido em binário é {n:b}')
    elif op == 2:
        print(f'O número {n} convertido em octal é {n:o}')
    elif op == 3:
        print(f'O número {n} convertido em hexadecimal é {n:X}')
    else:
        print('\033[31mOperação inválida\033[m')
else:
    print('\033[31mNúmero inválido\033[m')
