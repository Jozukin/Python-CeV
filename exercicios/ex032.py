ano = input('Digite um ano: ')
if not ano.isdigit():
    print('ERRO. Ano inválido')
else:
    ano = int(ano)
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano de {ano} é bissexto')
    else:
        print(f'o ano de {ano} não é bissexto')
