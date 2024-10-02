s = 0
qtdmulheres = 0
for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Sexo [M/F]: ').lower()
    s = s + idade
    if sexo == 'm':
        if c == 0:
            maiornomeh = nome
            maioridadeh = idade
        if (c != 0) and (idade > maioridadeh):
            maioridadeh = idade
            maiornomeh = nome
    elif sexo == 'f':
        if idade < 20:
            qtdmulheres = qtdmulheres + 1

print(f'A média de idade é {s/4} anos')
print(f'{maiornomeh} é o homem mais velho com {maioridadeh} anos')
print(f'{qtdmulheres} mulheres são menores que 20 anos')
