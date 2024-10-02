n1 = int(input('Qual o primeiro termo que deseja saber a progressão? '))
r = int(input('Qual a razão de progressão? '))
for c in range(1, 11):
    n = n1 + (c - 1) * r
    print(f'O termo {c} da progressão é {n}')
