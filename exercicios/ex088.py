from random import randint
listaJogos = []
print('='*40)
print(f'{'Gerador de jogos da MEGASENA':^40}')
print('='*40)
qtd = int(input('Quantos jogos deseja criar? '))
for c in range(0, qtd):
    jogo = []
    for volante in range(0, 6):
        if volante == 0:
            jogo.append(randint(1, 60))
        elif volante > 0:
            n = randint(1, 60)
            while n in jogo:
                n = randint(1, 60)
            jogo.append(n)
        jogo.sort()
    listaJogos.append(jogo)
for j in range(0, qtd):
    print(f'Jogo {j+1}: {listaJogos[j]}')

