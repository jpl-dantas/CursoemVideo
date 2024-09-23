def fatorial(n, show=False):
    """
        -> Esta função retorna o fatorial de qualquer valor.
        Também vem com uma função adicional que permite que você veja o cálculo do fatorial.
    :param n: número para o cálculo.
    :param show: exibição opcional do processo do cálculo fatorial.
    :return: resultado do valor fatorial de um número n.
    """

    from math import factorial
    f = factorial(n)
    if show:
        nc = n
        print(f'{n}! = {n} x ', end='')
        for c in range(n - 1, 1, -1):
            print(c, end=' x ')
            nc = nc * c
        print('1 =', end=' ')
    return f


print('-' * 30)
print(fatorial(5))
help(fatorial)
