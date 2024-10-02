from unidecode import unidecode
frase00 = input('Digite uma frase: ').strip().lower()
frase0 = unidecode(frase00)
frase = frase0.replace(' ', '')
if frase == frase[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
