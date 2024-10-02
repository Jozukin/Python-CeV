from modulos.moeda import aumentar, reduzir, dobro, metade, fmoeda, resumo
from modulos.dados import is_float
while True:
    valor = input('Digite o preço: R$')
    if is_float(valor):
        valor = float(valor)
        break
while True:
    porc_aum = input('Digite o valor da porcentagem do seu aumento: ')
    if is_float(porc_aum):
        porc_aum = float(porc_aum)
        break
while True:
    porc_red = input('Digite o valor da porcentagem da sua redução: ')
    if is_float(porc_red):
        porc_red = float(porc_red)
        break
print(f'A metade de {fmoeda(valor)} é {metade(valor, formatar=True)}')
print(f'O dobro de {fmoeda(valor)} é {dobro(valor, formatar=True)}')
print(f'O valor {fmoeda(valor)} com o aumento de {porc_aum}% é {aumentar(valor, porc_aum, formatar=True)}')
print(f'O valor {fmoeda(valor)} com a redução de {porc_red}% é {reduzir(valor, porc_red, formatar=True)}')
resumo(valor, porc_aum, porc_red)
