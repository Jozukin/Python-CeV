from modulos.moeda import aumentar, reduzir, dobro, metade, fmoeda, resumo
valor = float(input('Digite o preço: R$'))
while True:
    porc_aum = input('Digite o valor da porcentagem do seu aumento: ')
    if porc_aum.isnumeric():
        porc_aum = float(porc_aum)
        break
while True:
    porc_red = input('Digite o valor da porcentagem da sua redução: ')
    if porc_red.isnumeric():
        porc_red = float(porc_red)
        break
print(f'A metade de {fmoeda(valor)} é {metade(valor, formatar=True)}')
print(f'O dobro de {fmoeda(valor)} é {dobro(valor, formatar=True)}')
print(f'O valor {fmoeda(valor)} com o aumento de {porc_aum}% é {aumentar(valor, porc_aum, formatar=True)}')
print(f'O valor {fmoeda(valor)} com a redução de {porc_red}% é {reduzir(valor, porc_red, formatar=True)}')
resumo(valor, porc_aum, porc_red)
