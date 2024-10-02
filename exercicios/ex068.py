from random import randint
flag = 'venceu'
cont = 0
while flag == 'venceu':
    print(f'{' Jogo de par ou ímpar ':=^50}')
    jogador = int(input('Digite um número: '))
    print('Você escolhe par ou ímpar?')
    print('[ P ] Par')
    print('[ I ] Ímpar')
    op = input('Sua escolha: ').strip()
    computador = randint(1, 10)
    soma = jogador + computador
    print(f'O computador escolheu {computador}')
    print(f'{jogador} + {computador} é igual a {soma}')
    cont = cont + 1
    if op in 'Pp':
        if soma % 2 == 0:
            print(f'{soma} é PAR')
            print('Parabéns, você venceu!')
        else:
            print(f'{soma} é ÍMPAR')
            print('Você perdeu...')
            flag = 'perdeu'
    elif op in 'Ii':
        if soma % 2 == 0:
            print(f'{soma} é PAR')
            print('Você perdeu...')
            flag = 'perdeu'
        else:
            print(f'{soma} é ÍMPAR')
            print('Parabéns, você venceu!')
    else:
        print('Mas não foi escolhida uma opção válida')
if cont == 1:
    print('Você perdeu na primeira tentativa... Que pena.')
else:
    print(f'Você venceu {cont-1} vezes seguidas!')
