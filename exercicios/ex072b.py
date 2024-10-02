from num2words import num2words
n = int(input('Digite um número que deseja saber a escrita: '))
print(f'O número {n} por extenso é: {num2words(n, lang='pt-br')}')
