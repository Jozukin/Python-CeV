brasileirao = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athletico-PR', 'Red Bull Bragantino', 'Palmeiras',
               'Internacional', 'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Grêmio', 'Vasco', 'Fluminense',
               'Criciúma', 'Corinthians', 'Atlético-GO', 'Vitória', 'Cuiabá')
print(f'O G5 atual do brasileirão é composto por:')
for g in range(0, 5):
    print(f'{g+1}°: {brasileirao[g]}')
print('-' * 40)
print(f'O Z4 atual do brasileirão é composto por: ')
for z in range(16, 20):
    print(f'{z+1}°: {brasileirao[z]}')
print('-' * 40)
print('Os times participantes do brasileirão 2024 em ordem alfabética são:')
print(sorted(brasileirao))
print('-' * 40)
print(f'O Vasco está na posição {brasileirao.index('Vasco')+1}')
