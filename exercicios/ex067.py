n = 1
cont = 1
print(f'{' TABUADA ':=^40}')
print('\033[31mPara encerrar digite um número negativo\033[m')
while n >= 0:
    print('=' * 15) if cont == 10 else None
    n = int(input('Digite o número que deseja saber a tabuada: '))
    print('=' * 15) if n >= 0 else None
    cont = 1
    if n < 0:
        break
    while cont < 10:
        print(f'{n} x {cont} = {n*cont}')
        cont = cont + 1
