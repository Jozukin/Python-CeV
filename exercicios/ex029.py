vel = float(input('Qual a velocidade do carro? '))
via = float(input('Qual a velocidade máxima permitida na via? '))
if vel > via:
    print(f'Você foi Multado. Você ultrapassou a velocidade permitida da via em {vel-via}km/h')
    print(f'O valor da sua multa é de R${(vel-via)*7:.2f}')
else:
    print(f'Você não foi multado. Você estava a {via-vel}km/h abaixo da velocidade da via')
