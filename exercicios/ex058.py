import random
n = random.randint(0, 10)
erros = 1
n1 = int(input('Adivinhe qual número de 0 a 10 será sorteado: '))
while n1 != n:
    erros = erros + 1
    if n1 > n:
        n1 = int(input('Menos... Tente mais uma vez digitando outro número: '))
    elif n1 < n:
        n1 = int(input('Mais... Tente mais uma vez digitando outro número: '))
print(f'Parabéns, você acertou! O número sorteado foi {n} e você acertou com {erros} tentativas')
