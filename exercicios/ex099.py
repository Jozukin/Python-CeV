def maior(lst):  # usar (* num) para desempacotar vários números
    return max(lst)


qtd = int(input('Quantos valores deseja inserir? '))
numList = []
for c in range(0, qtd):
    num = numList.append(int(input(f'Digite o {c+1}° número: ')))

print(f'O maior número digitado foi {maior(numList)}')
