import datetime
ano0 = input('Digite seu ano de nascimento: ')
if len(ano0) == 4 and ano0.isdigit():
    ano = int(ano0)
    hoje = datetime.date.today().year
    if hoje - ano == 18:
        print('Você deve fazer seu alistamento militar ainda este ano.')
    elif hoje - ano < 18:
        faltam = 18 - (hoje - ano)
        print(f'Você deve se alistar daqui a {faltam} anos, no ano de {hoje+faltam}.')
    else:
        print('Se você ainda não se alistou, você está em atraso. Você precisa fazer seu alistamento.')
elif len(ano0) == 2 and ano0.isdigit():
    print('ERRO. O ano informado não está no formato de 4 dígitos')
else:
    print('\033[31mAno inválido\033[m')
