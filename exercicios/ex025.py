nome = input('Digite seu nome: ')
nomelower = nome.lower()
numnome = nomelower.find('silva')
if numnome >= 0:
    print('Seu nome possui "Silva"')
else:
    print('Seu nome não possui "Silva"')
