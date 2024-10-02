cidade = input('Digite o nome da sua cidade: ')
cidadelower = cidade.lower()
cidadesplit = cidadelower.split()
verif = cidadesplit[0].find('santo')
if verif != 0:
    print('Sua cidade não começa com "Santo"')
else:
    print('Sua cidade começa com "Santo"')
