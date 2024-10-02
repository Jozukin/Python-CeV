n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite um último número: '))
lista = [n1, n2, n3]
listasorted = sorted(lista)
print(f'O maior número digitado foi: {listasorted[2]}')
print(f'O menor número digitado foi: {listasorted[0]}')
