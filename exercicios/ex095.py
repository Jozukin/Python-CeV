todos = []
while True:
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
    todos.append(jogador)
    op = input('Quer continuar? [S/N] ')
    while op not in 'SsNn':
        op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break
print('='*60)
print(f'{'NO.':<4} {'NOME':<15} {'GOLS':<30} {'TOTAL':<10}')
for w, z in enumerate(todos):
    print(f'{w:<4} {todos[w]['nome']:<15} {str(todos[w]['gols']):<30} {todos[w]['total']:<20}')
print('='*60)
