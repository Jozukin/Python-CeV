lista = []
lista2 = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
for d in range(0, 5):
    lista2.append(min(lista))
    lista.pop(lista.index(min(lista)))
print(f'Sua lista de números ordenada é: {lista2}')
