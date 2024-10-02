def ajuda(funcao):
    print('\033[32m-\033[m' * (2 * (30 + len(funcao))))
    print(f'{f'\033[32mAcessando o manual do comando {funcao}\033[m':^{2 * (30 + len(funcao))}}')
    print('\033[32m-\033[m' * (2 * (30 + len(funcao))))
    print(f'\033[34m')
    help(funcao)
    print(f'\033[m')


while True:
    fun = input('Função ou Biblioteca > ').lower()
    if fun == 'fim':
        break
    ajuda(fun)
