n = int(input('Digite um número de termos para gerar em sua sequência de Fibonacci: '))
cont = 0
fiblist = [0, 1]
if n == 0:
    print('Digite um valor acima de zero')
elif n == 1:
    print('Sua sequência de Fibonacci é: [0]')
elif n == 2:
    print('Sua sequência de Fibonacci é: [0, 1]')
else:
    while cont < n - 2:
        a = fiblist[len(fiblist)-1] + fiblist[len(fiblist)-2]
        cont = cont + 1
        fiblist.append(a)
    print(f'Sua sequência de Fibonacci é: {fiblist}')
