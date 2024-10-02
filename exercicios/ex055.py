listapeso = []
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    listapeso.append(peso)
pesos = sorted(listapeso)
print(f'o menor é {pesos[0]} e o maior é {pesos[4]}')
