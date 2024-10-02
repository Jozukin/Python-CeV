palavras = ('variavel', 'funçao', 'biblioteca', 'sintaxe', 'classe', 'modulo', 'loop', 'objeto', 'estrutura', 'laços')
for c in range(0, 10):
    if 'a' or 'e' or 'i' or 'o' or 'u' in palavras[c]:
        print(f'As vogais da palavra {palavras[c]} são: ', end='')
        if 'a' in palavras[c]:
            print('a', end='')
        if 'e' in palavras[c]:
            print('e', end='')
        if 'i' in palavras[c]:
            print('i', end='')
        if 'o' in palavras[c]:
            print('o', end='')
        if 'u' in palavras[c]:
            print('u', end='')
        print('')
    else:
        print(f'A palavra {palavras[c]} não possui vogais')
