print('''Qual seu sexo?
[ M ] Masculino
[ F ] Feminino''')
sexo = input('').upper().strip()
if sexo:
    while sexo not in 'MF':
        sexo = input('Entrada inválida, digite [M] para masculino e [F] para feminino: ').upper().strip()
    print(f'Sexo {sexo} registrado com sucesso')
else:
    print('Entrada vazia, encerrando programa')
