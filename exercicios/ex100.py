from random import shuffle
from random import randint


def sorteio(lst):
    shuffle(lst)
    return lst[0:5]


def somapar(lst):
    s = 0
    for d, e in enumerate(lst):
        if e % 2 == 0:
            s += e
    return s


listaNum = []
for c in range(0, 10):
    listaNum.append(randint(0, 50))
lista = listaNum[:]
print(f'Números sorteados {lista}')
n = sorteio(listaNum)
print(f'5 números sorteados: {n}')
print(f'A soma dos pares sorteados foi: {somapar(n)}')





