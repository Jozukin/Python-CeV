def contagem(x, y, z):
    if z == 0:
        z = 1
    if z < 0:
        z = -z
    if x < y:
        print(f'Contagem de {x} até {y} de {z} em {z}:')
        for c in range(x, y+1, z):
            print(f'{c}', end=' ')
        print()
    elif y < x:
        z = -z
        print(f'Contagem de {x} até {y} de {-z} em {-z}:')
        for c in range(x, y-1, z):
            print(f'{c}', end=' ')
        print()
    else:
        print('Não é possível contagem entre 2 números iguais')


contagem(1, 10, 1)
print('='*40)
contagem(10, 1, 2)
print('='*40)

print('Agora é sua vez de pedir uma contagem: ')
a1 = int(input('Início: '))
a2 = int(input('Fim: '))
a3 = int(input('Passo: '))
contagem(a1, a2, a3)
