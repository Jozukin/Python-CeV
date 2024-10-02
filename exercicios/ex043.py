peso0 = input('Digite seu peso (em kg): ')
altura0 = input('Digite sua altura (em metros): ')
try:
    peso = float(peso0)
    altura = float(altura0)
    verif = 'true'
except ValueError:
    verif = 'false'
if verif == 'true':
    peso = float(peso0)
    altura = float(altura0)
    imc = peso / (altura**2)
    if imc <= 18.5:
        print(f'Seu IMC é {imc:.2f} e sua classificação com base no seu IMC é: \033[34mAbaixo do Peso\033[m')
    elif 25 >= imc > 18.5:
        print(f'Seu IMC é {imc:.2f} e sua classificação com base no seu IMC é: \033[34mPeso ideal\033[m')
    elif 30 >= imc > 25:
        print(f'Seu IMC é {imc:.2f} e sua classificação com base no seu IMC é: \033[34mSobrepeso\033[m')
    elif 40 >= imc > 30:
        print(f'Seu IMC é {imc:.2f} e sua classificação com base no seu IMC é: \033[34mObesidade\033[m')
    else:
        print(f'Seu IMC é {imc:.2f} e sua classificação com base no seu IMC é: \033[34mObesidade mórbida\033[m')
else:
    print('\033[31mNúmero inválido\033[m')
