n = int(input('Qual número deseja saber a tabuada? '))
print('Sua tabuada é:')
s = 0
for r in range(0, 9):
    s = s + 1
    print(f'{n}x{s} = {n * s}')
