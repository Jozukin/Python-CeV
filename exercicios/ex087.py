numeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
soma3col = 0
lista2col = []
for L in range(0, 3):
    for c in range(0, 3):
        n = numeros[L][c] = int(input(f'Digite um número na posição [{L}, {c}]: '))
        if n % 2 == 0:
            somaPares = somaPares + n
        if c == 2:
            soma3col = soma3col + n
        if L == 1:
            lista2col.append(n)
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[ {numeros[L][c]:^5} ]', end=' ')
        if c == 2:
            print()
print('='*40)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {soma3col}')
print(f'O maior valor da segunda linha é {max(lista2col)}')
