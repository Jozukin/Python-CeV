import random
seq = [0, 1, 2, 3, 4, 5] #random.randint(0, 5)
n = random.choice(seq)
n1 = int(input('Adivinhe qual número de 0 a 5 será sorteado: '))
if n1 == n:
    print(f'Parabéns, o número sorteado foi {n}')
else:
    print(f'Que pena... O número sorteado foi {n}')
