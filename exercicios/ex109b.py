from modulos.moeda import aumentar, reduzir, dobro, metade, fmoeda
porc = 0
valor = float(input('Digite o preço: R$'))
while True:
    print('''Digite a opção que deseja calcular:
    [ A ] Aumento
    [ R ] Redução
    [ N ] Não desejo calcular''')
    op = input('Sua escolha: ')
    while True:
        form = input('Deseja formatação? [S/N] ')
        if form in 'SsNn':
            break
    if op in 'AaRrNn':
        if op in 'Aa':
            while True:
                porc = input('Digite o valor da porcentagem do seu aumento: ')
                if porc.isnumeric():
                    porc = float(porc)
                    break
        elif op in 'Rr':
            while True:
                porc = input('Digite o valor da porcentagem da sua redução: ')
                if porc.isnumeric():
                    porc = float(porc)
                    break
        break

if form in 'Ss':
    print(f'A metade de {fmoeda(valor)} é {fmoeda(metade(valor))}')
    print(f'O dobro de {fmoeda(valor)} é {fmoeda(dobro(valor))}')
    if op in 'Aa':
        print(f'O valor {fmoeda(valor)} com o aumento de {fmoeda(porc)}% é {fmoeda(aumentar(valor, porc))}')
    elif op in 'Rr':
        print(f'O valor {fmoeda(valor)} com a redução de {fmoeda(porc)}% é {fmoeda(reduzir(valor, porc))}')
elif form in 'Nn':
    print(f'A metade de {valor} é {metade(valor)}')
    print(f'O dobro de {valor} é {dobro(valor)}')
    if op in 'Aa':
        print(f'O valor {valor} com o aumento de {porc}% é {aumentar(valor, porc)}')
    elif op in 'Rr':
        print(f'O valor {valor} com a redução de {porc}% é {reduzir(valor, porc)}')
