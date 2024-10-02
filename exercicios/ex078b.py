lista = []
maior = menor = 0
for c in range(1, 6):
    n = int(input('Digite um número: '))
    lista.append(n)
    if c == 1:
        posmaior = c
        posmenor = c
        maior = n
        menor = n
    else:
        if n > maior:
            posmaior = c
            maior = n
        if n < menor:
            posmenor = c
            menor = n
print(f'O maior valor digitado está na posição {posmaior} e foi: {max(lista)}')
print(f'O menor valor digitado está na posição {posmenor} foi: {min(lista)}')
