print('Calculadora para somar quantos números você desejar')
print('Para encerrar o programa digite o número 999')
c = 0
n = 0
s = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'A soma dos {c} números digitados foi de {s}')
