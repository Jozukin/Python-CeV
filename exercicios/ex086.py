numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for L in range(0, 3):
    for c in range(0, 3):
        numeros[L][c] = int(input(f'Digite um número na posição [{L}, {c}]: '))
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[ {numeros[L][c]:^5} ]', end=' ')
        if c == 2:
            print()
