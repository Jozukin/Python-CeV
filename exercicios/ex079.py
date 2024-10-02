lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    while op not in 'SN':
        op = input('Deseja continuar? [S/N] ').upper()
    if op in 'Nn':
        break
lista.sort()
print(lista)
