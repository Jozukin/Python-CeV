p = float(input('Qual o valor do produto?R$'))
d = float(input('Qual o valor do desconto? (somente números de 0 a 100) '))
valor = p * (1 - (d/100))
print(f'O valor do produto com desconto de {d}% é R${valor}')
