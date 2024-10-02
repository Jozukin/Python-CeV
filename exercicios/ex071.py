saque = int(input('Qual o valor que deseja sacar? R$'))
qtd50 = qtd20 = qtd10 = qtd1 = 0
while saque >= 50:
    saque = saque - 50
    qtd50 = qtd50 + 1
while saque >= 20:
    saque = saque - 20
    qtd20 = qtd20 + 1
while saque >= 10:
    saque = saque - 10
    qtd10 = qtd10 + 1
while saque >= 1:
    saque = saque - 1
    qtd1 = qtd1 + 1
print(f'Sacando {qtd50} cédulas de R$50, {qtd20} cédulas de R$20, {qtd10} cédulas de R$10 e {qtd1} cédulas de R$1.')
