produtos = ('Arroz', 'R$ 25,00', 'Feijão', 'R$ 10,00', 'Leite', 'R$ 4,50', 'Pão francês', 'R$ 12,00',
            'Manteiga', 'R$ 8,00', 'Frango', 'R$ 20,00', 'Tomate', 'R$ 7,00', 'Cebola', 'R$ 6,00',
            'Macarrão', 'R$ 5,00', 'Sabão em pó', 'R$ 15,00')
print(f'{' Compras ':=^50}')
for c in range(0, 20, 2):
    print(f'{produtos[c]:.<40}{produtos[c+1]}')
