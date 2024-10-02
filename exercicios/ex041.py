idade0 = input('Digite sua idade: ')
if idade0.isdigit():
    idade = int(idade0)
    if idade > 20:
        print('Sua categoria é: \033[34mMaster\033[m')
    elif 19 < idade <= 20:
        print('Sua categoria é: \033[34mSênior\033[m')
    elif 14 < idade <= 19:
        print('Sua categoria é: \033[34mJunior\033[m')
    elif 9 < idade <= 14:
        print('Sua categoria é: \033[34mInfantil\033[m')
    else:
        print('Sua categoria é: \033[34mMirim\033[m')
else:
    print('\033[31mIdade inválida\033[m')
