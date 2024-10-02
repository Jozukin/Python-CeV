from modulos.dados import leiaint
while True:
    print('~' * 40)
    print(f'{'MENU PRINCIPAL':^40}')
    print('~' * 40)
    print('''[ 1 ] Ver pessoas cadastradas
[ 2 ] Cadastrar novas pessoas
[ 3 ] Sair do sistema''')
    print('~' * 40)
    while True:
        op = leiaint('Sua escolha: ')
        if op == 1 or op == 2 or op == 3:
            break
        else:
            print('Escolha inválida. Digite 1, 2 ou 3.')
            print('~' * 40)
    if op == 2:
        while True:
            nome = input('Digite seu nome: ').strip()
            if nome != '':
                break
        while True:
            idade = input('Digite sua idade: ').strip()
            try:
                idade = int(idade)
            except ValueError:
                pass
            else:
                idade = str(idade)
                break
        lista = [nome, idade]
        with open('ex115a.txt', 'a') as arquivo:
            arquivo.writelines(nome)
            arquivo.writelines(',')
            arquivo.writelines(idade)
            arquivo.writelines(';')

    elif op == 1:
        print('~' * 40)
        print(f'{'Lista de pessoas cadastradas':^40}')
        print('~' * 40)
        print(f'{'NOME':<20}', end=' '*5)
        print(f'{'IDADE':>3}')

        with open("ex115a.txt", "r") as arquivo:
            conteudo = arquivo.read()
            pessoas = conteudo.split(';')
            pessoas.pop()
            for n, lst in enumerate(pessoas):
                parte = pessoas[n]
                ficha = parte.split(',')
                print(f'{ficha[0]:<20}', end=' '*5)
                print(f'{ficha[1]:>3}')

    elif op == 3:
        break
