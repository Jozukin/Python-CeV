def ficha(nome, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols no campeonato'


n = input('Digite o nome do jogador: ')
gol = input('Digite o número de gols do jogador: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

print(ficha(n, gol))


