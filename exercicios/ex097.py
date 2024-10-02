def escreva(msg):
    print('~'*len(msg)*2)
    print(f'{msg:^{len(msg)*2}}')
    print('~'*len(msg)*2)


m = input('Qual mensagem deseja escrever? ')
escreva(m)
