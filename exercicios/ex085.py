listaPares = []
listaImpares = []
lista = [listaPares, listaImpares]
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)
listaPares.sort()
listaImpares.sort()
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listaPares}')
print(f'A lista de ímpares é: {listaImpares}')
