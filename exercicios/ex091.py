from random import randint
# from operator import itemgetter - ordenar de outra forma
jogadores = []
maior = 0
for c in range(0, 4):
    nome = input(f'Digite o nome do jogador {c+1}: ')
    dado = randint(1, 6)
    jogador = {'nome': nome, 'dado': dado}
    jogadores.append(jogador)
    if c == 0:
        maior = dado
    elif c > 0:
        if dado >= maior:
            maior = dado
print()
for d, e in enumerate(jogadores):
    print(f'{jogadores[d]['nome']} tirou {jogadores[d]['dado']} no dado')
jogadores.sort(reverse=True, key=lambda x: x['dado'])
cont = 0
for d in range(0, len(jogadores)):
    if jogadores[d]['dado'] == maior:
        cont = cont + 1
print(f'\nO maior valor do dado foi {jogadores[0]['dado']}\n')
if cont > 1:
    print('EMPATE entre', end=' ')
    for g in range(0, cont):
        print(f'{jogadores[g]['nome']}', end=' ')
        if g < cont-1:
            print('e', end=' ')
        else:
            break
else:
    print(f'O jogador {jogadores[0]['nome']} foi o vencedor')
