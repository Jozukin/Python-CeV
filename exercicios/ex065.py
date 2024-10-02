op = 'S'
nlist = []
cont = 0
s = 0
while op in 'Ss':
    n = float(input(f'Digite o {cont+1}° número: '))
    cont = cont + 1
    nlist.append(n)  # para armazenar de outra forma usar "if n > maior, maior = n"
    s = s + n
    if len(nlist) > 1:
        op = input('Deseja continuar? [S/N]: ').strip()
if op in 'Nn':
    print(f'A média dos {cont} valores digitados foi de {s/cont}')
    print(f'O maior valor digitado foi {max(nlist)}')
    print(f'O menor valor digitado foi {min(nlist)}')
else:
    print('Entrada inválida')
