def leiaint(msg):
    while True:
        num = input(msg)
        try:
            num = int(num)
            return num
        except ValueError:
            print('ERRO. Digite um número inteiro válido.')


def leiafloat(msg):
    while True:
        num = input(msg)
        try:
            num = float(num)
            return num
        except ValueError:
            print('ERRO. Digite um número real válido.')


n = leiaint('Digite um número: ')
n2 = leiafloat('Digite um número float: ')
print(f'Você digitou o número inteiro {n}')
print(f'Você digitou o número real {n2}')
