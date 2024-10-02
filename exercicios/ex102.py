def fatorial(fat, show=False):
    """-> Calcula o FATORIAL de um número
    :param fat: O número a ser calculado
    :param show: (opcional) mostrar a conta na tela
    :return: o valor fatorial de um número n."""
    s = 1
    nums = [fat]
    if fat == 0 or fat == 1:
        if not show:
            return 1
        elif show and fat == 0:
            return '0! = 1'
        elif show and fat == 1:
            return '1! = 1'
    while fat > 0:
        s *= fat
        fat -= 1
        nums.append(fat)
        if fat == 0:
            if not show:
                return s
        if fat == 0:
            if show:
                n = f'{nums[0]}! = '
                for c in range(0, len(nums)-1):
                    if c < len(nums)-2:
                        n = n + f'{nums[c]} x '
                    if c == len(nums)-2:
                        n = n + f'1 = {s}'
                return n


print(fatorial(2, show=True))
help(fatorial)
