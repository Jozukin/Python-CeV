lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
print(f'O {lista.index(max(lista))+1}° número foi o maior, com o valor de: {max(lista)}')
print(f'O {lista.index(min(lista))+1}° número foi o menor, com o valor de: {min(lista)}')
