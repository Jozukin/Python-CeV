def leiaint(msg):
    while True:
        num = input(msg)
        if num.isdigit():
            return int(num)
        else:
            print('ERRO. Digite um número inteiro válido.')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
