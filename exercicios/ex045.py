import random
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
cpu = random.choice(lista)
print('\033[36m=\033[m'*5, '\033[35mTENTE ME VENCER NO PEDRA, PAPEL OU TESOURA!\033[m', '\033[36m=\033[m'*5)
player = input('Digite \033[36m"pedra"\033[m, \033[36m"papel"\033[m ou \033[36m"tesoura"\033[m: ').strip().lower()
if player == 'pedra' or player == 'papel' or player == 'tesoura':
    print('')
    print('O cpu está escolhendo...')
    sleep(2)
    print('')
    print(f'O cpu escolheu \033[36m{cpu}\033[m.')
    print('')
    if player == 'pedra':
        if cpu == 'pedra':
            print('\033[33mEmpate\033[m')
        elif cpu == 'papel':
            print('\033[31mVocê perdeu...\033[m')
        else:
            print('\033[34mVocê venceu!\033[m')
    elif player == 'papel':
        if cpu == 'pedra':
            print('\033[34mVocê venceu!\033[m')
        elif cpu == 'papel':
            print('\033[33mEmpate\033[m')
        else:
            print('\033[31mVocê perdeu...\033[m')
    elif player == 'tesoura':
        if cpu == 'pedra':
            print('\033[31mVocê perdeu...\033[m')
        elif cpu == 'papel':
            print('\033[34mVocê venceu!\033[m')
        else:
            print('\033[33mEmpate\033[m')
else:
    print('\033[31mEntrada inválida\033[m')
