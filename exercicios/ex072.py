n = int(input('Digite um número de 0 a 20 que deseja saber a escrita: '))
while n > 20 or n < 0:
    n = int(input('Número inválido. Tente novamente: '))
nomes = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'O número {n} em sua forma escrita é {nomes[n]}')
