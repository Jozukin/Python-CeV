def area(x, y):
    h = x * y
    return h


print('Quais as dimensões do seu terreno?')
a = float(input('Largura: '))
b = float(input('Comprimento: '))

print(f'O valor da área é {area(a, b)}')
