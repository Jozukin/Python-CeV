from modulos.moeda import aumentar, reduzir, dobro, metade, fmoeda, resumo
from modulos.dados import leiadinheiro

valor = leiadinheiro('Digite o preço: R$')
porc_aum = leiadinheiro('Digite o valor da porcentagem do seu aumento: ')
porc_red = leiadinheiro('Digite o valor da porcentagem da sua redução: ')

print(f'A metade de {fmoeda(valor)} é {metade(valor, formatar=True)}')
print(f'O dobro de {fmoeda(valor)} é {dobro(valor, formatar=True)}')
print(f'O valor {fmoeda(valor)} com o aumento de {porc_aum}% é {aumentar(valor, porc_aum, formatar=True)}')
print(f'O valor {fmoeda(valor)} com a redução de {porc_red}% é {reduzir(valor, porc_red, formatar=True)}')
resumo(valor, porc_aum, porc_red)
