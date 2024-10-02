viagem = float(input('Qual a distância da viagem em km? '))
if viagem > 200:
    preco = viagem * 0.45
    print(f'O valor da sua passagem é de R${preco}')
else:
    preco = viagem * 0.50
    print(f'O valor da sua passagem é de R${preco}')
