lista = []
exp = input('Digite uma expressão matemática com uso de parênteses: ')
if exp.index(')') < exp.index('('):
    print('Expressão inválida')
else:
    if exp.count(')') != exp.count('('):
        print('Expressão inválida')
    else:
        if exp[::-1].index(')') > exp[::-1].index('('):
            print('Expressão inválida')
        else:
            print('Expressão válida')


