rr1 = input('Digite o valor de uma reta: ')
rr2 = input('Digite o valor de outra reta: ')
rr3 = input('Digite o valor da última reta: ')
try:
    r1 = float(rr1)
    r2 = float(rr2)
    r3 = float(rr3)
    verif = 'true'
except ValueError:
    verif = 'false'
if verif == 'true':
    r1 = float(rr1)
    r2 = float(rr2)
    r3 = float(rr3)
    iguais = 'sim' if r1 == r2 == r3 else 'nao'
    if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
        print('Um triângulo pode ser construído com essas 3 retas')
        if (r1 == r2 or r1 == r3 or r2 == r3) and iguais == 'nao':
            print('O triângulo construído é \033[34mISÓSCELES\033[m')
        elif iguais == 'sim':
            print('O triângulo construído é \033[34mEQUILÁTERO\033[m')
        else:
            print('O triângulo construído é \033[34mESCALENO\033[m')
    else:
        print('Não é possível construir um triangulo com essas 3 retas')
else:
    print('\033[31mNúmero inválido\033[m')
