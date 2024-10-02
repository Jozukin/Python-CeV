b = ()
tuplaPar = ()
tuplaPares = ()
pares = 0
for c in range(0, 4):
    n = input(f'Digite o {c+1}° valor: ')
    while not n.isdigit():
        n = input(f'Valor inválido, digite o {c+1}° valor novamente: ')
    if int(n) % 2 == 0:
        pares = pares + 1
        tuplaPar = (int(n),)
        tuplaPares = tuplaPares + tuplaPar
    n = (int(n),)
    b = b + n
print(f'O valor 9 apareceu {b.count(9)} vezes')
try:
    indice = b.index(3)
    print(f'O valor 3 foi digitado pela primeira vez na posição {indice+1}')
except ValueError:
    print('O valor 3 não foi encontrado na tupla')
if len(tuplaPares) == 1:
    print(f'Foi digitado {pares} número par, sendo ele: {tuplaPares[0]}')
elif len(tuplaPares) == 0:
    print('Não foi digitado nenhum número par')
elif len(tuplaPares) > 1:
    print(f'foram digitados {pares} números pares, sendo eles: {tuplaPares}')
