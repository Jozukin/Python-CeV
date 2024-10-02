import random
seq = ['pedro', 'xines', 'davi', 'leo']
n = random.choice(seq)
print('Quem disse a seguinte frase:')
if n == 'xines':
    print('Posso falar mais nada então')
elif n == 'pedro':
    print('Já deu 20:30?')
elif n == 'davi':
    print('Bora jogar lol? (por 10 minutos)')
elif n == 'leo':
    print('Quando eu entrar de férias eu vou encher a cara')
resp = (input('Resposta: ')).lower()
if resp == n:
    print(f'Parabéns, a resposta era {n}')
else:
    print(f'Você errou, a resposta era {n}')
