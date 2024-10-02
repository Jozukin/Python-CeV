lista = []
soma = 0
while True:
    pessoa = {}
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: [M/F] ').upper()
    while sexo not in 'MmFf':
        sexo = input('Digite seu sexo? [M/F] ').upper()
    idade = int(input('Digite sua idade: '))
    soma = soma + idade
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    lista.append(pessoa)
    op = input('Deseja continuar? [S/N] ')
    while op not in 'SsNn':
        op = input('Deseja continuar? [S/N] ')
    if op in 'Nn':
        break
media = soma/(len(lista))
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é {media}')
listaF = []
listaMedia = []
for x in lista:
    for y, z in x.items():
        if y == 'sexo':
            if x['sexo'] in 'Ff':
                listaF.append(x['nome'])
        if y == 'idade':
            if x['idade'] > media:
                listaMedia.append(x['nome'])
print(f'As mulheres inseridas foram: {listaF}')
print(f'As pessoas acima da média de idade foram: {listaMedia}')
