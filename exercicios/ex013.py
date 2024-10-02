s = float(input('Qual seu salário (em reais)? '))
a = float(input('Qual o a porcentagem de aumento? (apenas números) '))
total = s * (1 + (a/100))
print(f'O valor do salário com o aumento é de {total}')
