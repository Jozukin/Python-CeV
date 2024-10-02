turma = []
listaAlunos = []
listaNotas = []
medias = []
while True:
    nome = input('Digite o nome do aluno: ').upper()
    listaAlunos.append(nome)
    for n in range(1, 3):
        nota = float(input(f'Digite a {n}° nota: '))
        listaNotas.append(nota)
    listaAlunos.append(listaNotas[:])
    medias.append((listaNotas[0]+listaNotas[1])/2)
    listaNotas.clear()
    turma.append(listaAlunos[:])
    listaAlunos.clear()
    op = input('Deseja inserir outro aluno? [S/N] ')
    while op not in 'SsNn':
        op = input('Deseja inserir outro aluno? [S/N] ')
    if op in 'Nn':
        break
print(f'{'No.':<4} {'NOME':<20} {'MÉDIA':<20}')
print('='*40)
for a in range(0, len(turma)):
    print(f'{a:<4} {turma[a][0]:<20} {medias[a]:<20}')
print('='*40)
while True:
    nAluno = input(f'Qual aluno você deseja saber as notas? [de 0 a {len(turma)-1}] ')
    while (len(turma) - 1) < int(nAluno) < 0:
        nAluno = input(f'Aluno não encontrado, tente novamente: [de 0 a {len(turma)-1}] ')
    nAluno = int(nAluno)
    print(f'o aluno {turma[nAluno][0]} possui as notas {turma[nAluno][1][0]} e {turma[nAluno][1][1]}')
    op2 = input('Deseja buscar por outro aluno? [S/N] ')
    while op2 not in 'SsNn':
        op2 = input('Deseja buscar por outro aluno? [S/N] ')
    if op2 in 'Nn':
        break
