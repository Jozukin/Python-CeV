flag = 's'
total = cont = menor = qtd1000 = 0
num = 1
nomemenor = ''
while flag in 'Ss':
    nome = input(f'Qual o nome do {num}° produto? ')
    preco = float(input('Qual o valor do produto? R$').replace(',', '.'))
    total = total + preco
    cont = cont + 1
    num = num + 1
    if cont == 1:
        menor = preco
        nomemenor = nome
    elif cont > 1:
        if preco < menor:
            menor = preco
            nomemenor = nome
    if preco > 1000:
        qtd1000 = qtd1000 + 1
    flag = input('Deseja inserir mais produtos? [S/N] ')
    while flag not in 'SsNn':
        flag = input('Deseja inserir mais produtos? [S/N] ')
print(f'{nomemenor} é o produto mais barato com o valor de R${menor:.2f}')
print(f'O valor total dos {cont} produtos é de R${total:.2f}')
print(f'{qtd1000} produtos custam mais que R$1000')
