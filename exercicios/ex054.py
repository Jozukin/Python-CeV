import datetime
ano = datetime.date.today().year
x = 0
for c in range(0, 7):
    n = int(input('Digite seu ano de nascimento: '))
    idade = ano - n
    if idade >= 18:
        x = x + 1
print(f'{x} pessoas são maiores de idade')
