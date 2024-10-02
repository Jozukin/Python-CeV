rnota1 = input('Digite a nota 1: ')
rnota2 = input('Digite a nota 2: ')
try:
    nota1 = float(rnota1)
    nota2 = float(rnota2)
    verif = 'true'
except ValueError:
    verif = 'false'
if verif == 'true':
    nota1 = float(rnota1)
    nota2 = float(rnota2)
    media = (nota1+nota2)/2
    if media >= 7:
        print('\033[34mAluno APROVADO\033[m')
    elif media < 5:
        print('\033[31mAluno REPROVADO\033[m')
    else:
        print('\033[33mAluno de RECUPERAÇÃO\033[m')
else:
    print('\033[31mNota inválida\033[m')
