from datetime import date
anohoje = date.today().year
nome = input('Qual seu nome? ')
ano = int(input('Qual seu ano de nascimento? '))
idade = anohoje - ano
carteira = int(input('Qual o número da sua carteira de trabalho? [Digite 0 caso não possua] '))
if carteira == 0:
    carteira = 'não possui'
    pessoa = {'nome': nome, 'idade': idade, 'carteira': carteira}
    aposentText = 'Você precisa de 35 anos de contribuição para se aposentar'
else:
    salario = float(input('Qual seu salário? R$'))
    anoContrat = int(input('Qual foi o ano da sua primeira contratação? '))
    anoContrib = anoContrat + 35
    aposent = anoContrib - anohoje
    pessoa = {'nome': nome, 'idade': idade, 'carteira': carteira, 'contratação': anoContrat, 'salário': salario}
    if aposent <= 0:
        aposentText = 'Você já pode se aposentar'
    else:
        aposentText = f'Você ainda precisa trabalhar {aposent} anos para se aposentar'

print(pessoa)
for x, y in pessoa.items():
    print(f'{x} é {y}')
print(aposentText)
