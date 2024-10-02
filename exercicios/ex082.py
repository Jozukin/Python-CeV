lista = []
listaPar = []
listaImpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    while op not in 'SsNn':
        op = input('Deseja continuar? [S/N] ').upper()
    if op in 'Nn':
        break
for num in lista:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'Lista original: {lista}')
print(f'Pares digitados: {listaPar}')
print(f'Ímpares digitados: {listaImpar}')
