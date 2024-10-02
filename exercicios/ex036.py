rcasa = input('Qual o valor da casa que deseja comprar? R$')
rsalario = input('Quanto é seu salário? R$')
rano = input('Em quantos anos você pretende pagar? ')
try:
    casa = float(rcasa)
    salario = float(rsalario)
    ano = float(rano)
    verif = 'true'
except ValueError:
    verif = 'falso'
if verif == 'true':
    casa = float(rcasa)
    salario = float(rsalario)
    ano = float(rano)
    salario30 = salario * 0.30
    parcela = casa / (ano * 12)
    if parcela <= salario30:
        print(f'O empréstimo está \033[32mDISPONÍVEL\033[m para você. Você pagará R${parcela:.2f} por mês', end=' ')
        print(f'durante {ano} anos.')
    else:
        print(f'Seu empréstimo foi \033[31mNEGADO\033[m por conta da parcela (R${parcela:.2f})', end=' ')
        print(f'exceder 30% de seu salário (R${salario30:.2f})')
else:
    print("\033[31mNúmero Inválido\033[m")
