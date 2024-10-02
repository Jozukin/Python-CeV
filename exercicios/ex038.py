n1r = input('Digite um número: ')
n2r = input('Digite outro número: ')
if n1r.isdigit() and n2r.isdigit():
    n1 = int(n1r)
    n2 = int(n2r)
    if n1 > n2:
        print(f'O primeiro valor \033[34m[{n1}]\033[m é maior que o segundo valor \033[35m[{n2}]\033[m')
    elif n2 > n1:
        print(f'O segundo valor \033[35m[{n2}]\033[m é maior que o primeiro valor \033[34m[{n1}]\033[m')
    else:
        print(f'Os dois valores são iguais')
else:
    print('\033[31mNúmero Inválido\033[m')
