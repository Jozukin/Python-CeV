import random
grupo1 = input('Qual o líder do grupo 1? ')
grupo2 = input('Qual o líder do grupo 2? ')
grupo3 = input('Qual o líder do grupo 3? ')
grupo4 = input('Qual o líder do grupo 4? ')
grupo5 = input('Qual o líder do grupo 5? ')
lista = [grupo1, grupo2, grupo3, grupo4, grupo5]
print(f'A ordem de apresentação é: {random.sample(lista, 5)}')
