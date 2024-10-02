salario = float(input('Qual seu salário? R$'))
if salario > 1250:
    novosalario = salario * 1.10
    print(f'Seu novo salário é de R${novosalario:.2f}')
else:
    novosalario = salario * 1.15
    print(f'Seu novo salário é de R${novosalario:.2f}')
