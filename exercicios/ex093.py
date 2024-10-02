gols = []
nome = input('Qual o nome do jogador? ')
jogos = int(input(f'Quantas partidas {nome} jogou? '))
jogador = {'nome': nome}
for c in range(0, jogos):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(gol)
total = sum(gols)
jogador['gols'] = gols
jogador['total'] = total
print('='*30)
print(jogador)
print('='*30)
for x, y in jogador.items():
    print(f'O campo {x} tem o valor {y}')
