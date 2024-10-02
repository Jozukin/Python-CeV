def voto(ano):
    from datetime import date
    idade_local = date.today().year - ano
    if 18 <= idade_local < 65:
        return 'OBRIGATÓRIO'
    elif 16 <= idade_local < 18 or idade_local >= 65:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


while True:
    idade = input('Digite seu ano de nascimento: ').strip()
    if int(len(idade)) == 4 and idade.isdigit():
        idade = int(idade)
        break
print(f'Seu voto é {voto(idade)}')

