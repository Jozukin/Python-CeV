n = input('Digite seu nome: ')
nome = n.strip()
print(f'Seu nome em letras minúsculas é {nome.lower()} e em letras maiúsculas é {nome.upper()}')
lennome = len(nome)
contspace = nome.count(' ')
contnome = lennome - contspace
findspace = nome.find(' ')
primeiro = len(nome[:findspace])
print(f'Seu primeiro nome tem {primeiro} letras e seu nome completo tem {contnome} letras')
# alternativa: usar split pra dividir o nome
