f0 = input('Digite uma frase: ')
f = f0.strip()
frase = f.lower()
let0 = input('Qual letra deseja fazer a contagem? ')
let = let0.strip()
letra = let.lower()
count = frase.count(letra)
posicaoi = frase.find(letra)
posicaoinvf = frase[::(-1)].find(letra)
posicaof = (len(frase) - posicaoinvf) - 1
print(f'A letra "{letra}" apareceu {count} vezes na frase. Sua primeira aparição foi na posição {posicaoi}', end=' ')
print(f'e a última aparição foi na posição {posicaof}')
