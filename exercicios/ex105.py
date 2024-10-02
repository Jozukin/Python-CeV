def notas(*num, sit=False):
    """Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas que serão digitadas
    :param sit: (opcional) Mostrar ou não a situação do aluno.
    :return: Dicionário com várias informações sobre o aluno."""
    maior = max(num)
    menor = min(num)
    qtd = len(num)
    media = sum(num)/len(num)
    situ = ''
    if media >= 7:
        situ = 'APROVADO'
    elif media < 7:
        situ = 'REPROVADO'
    if sit:
        return {'total': qtd, 'maior': maior, 'menor': menor, 'média': media, 'situação': situ}
    else:
        return {'total': qtd, 'maior': maior, 'menor': menor, 'média': media}


print(notas(5, 4, 3, sit=True))
