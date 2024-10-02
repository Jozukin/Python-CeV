nome = input('Digite o nome do aluno: ')
media = float(input('Qual sua média? ').replace(',', '.'))
if media >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
alunos = {'nome': nome, 'média': media, 'situação': situacao}
print(alunos)
