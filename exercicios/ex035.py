r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite o valor da última reta: '))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Um triângulo pode ser construído com essas 3 retas')
else:
    print('Não é possível construir um triangulo com essas 3 retas')
