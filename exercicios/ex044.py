preco0 = input('Informe o valor do produto: R$')
print('Tipos de pagamento:\n1 = à vista (dinheiro)/pix [10% de desconto]\n2 = à vista (cartão) [5% de desconto]')
print('3 = 2x no cartão\n4 = 3x à 12x no cartão [20% juros]')
pag0 = input('Informe o tipo de pagamento: ')
try:
    preco = float(preco0)
    pag = int(pag0)
    verif = 'true'
except ValueError:
    verif = 'false'
if verif == 'true':
    preco = float(preco0)
    pag = int(pag0)
    if pag == 1:
        precofinal = preco * 0.90
        print(f'O valor final do seu produto com 10% de desconto é R${precofinal:.2f}')
    elif pag == 2:
        precofinal = preco * 0.95
        print(f'O valor final do seu produto com 5% de desconto é de R${precofinal:.2f}')
    elif pag == 3:
        precofinal = preco
        print(f'O valor final do seu produto é de R${precofinal:.2f}')
    elif pag == 4:
        precofinal = preco * 1.20
        print(f'O valor final do seu produto é de R${precofinal:.2f}')
    else:
        print('\033[31mTipo de pagamento inválido\033[m')
else:
    print('\033[31mNúmero inválido\033[m')
