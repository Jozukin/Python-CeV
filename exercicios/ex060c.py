n = int(input('Digite o número que deseja saber o fatorial: '))
fat = n
multi = n
if n == 0 or n == 1:
    print(f'O fatorial de {n} é 1')
else:
    for c in range(1, fat):
        fat = fat - 1
        multi = multi * fat
    print(f'o fatorial de {n} é {multi}')
