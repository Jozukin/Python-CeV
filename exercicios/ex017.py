import math
copo = float(input('Qual o valor do cateto oposto? '))
cadj = float(input('Qual o valor do cateto adjacente? '))
hip = math.sqrt(((copo**2) + (cadj**2)))
print(f'O valor da hipotenusa é de {hip}')
