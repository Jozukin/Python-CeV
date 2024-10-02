lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    if op not in 'SsNn':
        op = input('Deseja continuar? [S/N] ').upper()
    if op in 'Nn':
        break
lista.sort(reverse=True)
print(f'Os {len(lista)} números digitados em ordem decrescente foram: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi encontrado na lista')
