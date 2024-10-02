n18 = nhomens = nmulheres20 = 0
cont = 1
flag = 's'
while flag in 'Ss':
    print(f'Digite os dados da {cont}° pessoa: ')
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo? [M/F] ')
    while sexo not in 'MmFf':
        sexo = input('Sexo Inválido. Qual seu sexo? [M/F] ')
    cont = cont + 1
    if sexo in 'Mm':
        nhomens = nhomens + 1
    if sexo in 'Ff' and idade < 20:
        nmulheres20 = nmulheres20 + 1
    if idade >= 18:
        n18 = n18 + 1
    flag = input('Deseja continuar? [S/N] ')
    while flag not in "SsNn":
        flag = input('Deseja continuar? [S/N] ')
print(f'{n18} pessoas tem 18 anos ou mais')
print(f'{nhomens} pessoas são homens')
print(f'{nmulheres20} mulheres tem menos que 20 anos')
