pessoas = []
qtdpessoas = 0
maiorPesoNome = []
menorPesoNome = []
while True:
    nome = input('Qual seu nome? ')
    peso = int(input('Quanto você pesa? '))
    individuo = [nome, peso]
    pessoas.append(individuo)
    qtdpessoas = qtdpessoas + 1
    op = input('Deseja inserir mais pessoas? [S/N] ')
    while op not in 'SsNn':
        op = input('Deseja inserir mais pessoas? [S/N] ')
    if op in 'Nn':
        break
maiorPeso = max(pessoas, key=lambda x: x[1])[1]
menorPeso = min(pessoas, key=lambda x: x[1])[1]
for p in pessoas:
    if p[1] == maiorPeso:
        maiorPesoNome.append(p[0])
    elif p[1] == menorPeso:
        menorPesoNome.append(p[0])
print(f'{qtdpessoas} pessoas foram cadastradas')
print(f'As pessoas mais pesadas foram {maiorPesoNome} com {maiorPeso}kg')
print(f'As pessoa mais leves foram {menorPesoNome} com {menorPeso}kg')
