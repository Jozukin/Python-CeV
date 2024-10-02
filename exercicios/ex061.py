n1 = int(input('Qual o primeiro termo que deseja saber a progressão? '))
r = int(input('Qual a razão de progressão? '))
n = n1
termo = 1
print(f'O 1° termo da progressão é {n1}')
while termo < 10:
    n = n + r
    termo = termo + 1
    print(f'O {termo}° termo da progressão é {n}')
print('Você deseja saber mais termos após o 10°?')
op = int(input('Digite a quantidade que deseja saber ou digite 0 para encerrar: '))
if op > 0:
    while termo < 10 + op:
        n = n + r
        termo = termo + 1
        print(f'O {termo}° termo da progressão é {n}')
elif op == 0:
    print('Programa encerrado.')
