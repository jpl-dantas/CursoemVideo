def lin(c, q=34):
    """
    Este comando criará uma linha reta horizontal com a quantidade e o caractere desejado.

    :param c: c recebe o caractere que será multiplicado formando uma linha reta horizontal;
    :param q: q recebe a quantidade de vezes que o caractere será multiplicado;
    :return: retorna a linha criada.
    """
    return f'{c}' * q


def custom(s=0, t=30, b=40, sit=False):
    """
    Este comando serve para facilitar o processo de customizar o texto do python.

    :param s: s recebe o estilo da fonte;
    :param t: t recebe a cor do texto;
    :param b: b recebe a cor de fundo do texto;
    :param sit: False: cria a customização desejada | True: encerra a customização na linha de código.
    :return: retorna a customização criada.
    """
    if not sit:
        return f'\033[{s}:{t}:{b}m'
    else:
        return '\033[m'


def inhel():
    """
    Esta função é uma automatizadora da função help(). O usurário poderá solicitar a documentação de qualquer função/
    biblioteca infinitamente, a função é encerrada apenas quando o usuário digitar "fim".

    :return:
    """
    print(f'{custom(1, 30, 44)}{lin("=")}')
    print('     SISTEMA INTERACTIVE HELP')
    print(lin('='))
    key = ''
    while key != 'fim':
        key = input(f'{custom(sit=True)}Digite um comando para ver suas instruções > ').lower()
        if key == 'fim':
            custom(sit=True)
            break
        else:
            print(f'{custom(0, 30, 45)}{lin("-")}')
            print(f'{help(key)}')
            print(lin('-'))
    print(f'{custom(1, 30, 41)}{lin("=", len("    OBRIGADO POR UTILIZAR O NOSSO SISTEMA") + 4)}')
    print('   OBRIGADO POR UTILIZAR O NOSSO SISTEMA')
    print(lin('=', len('    OBRIGADO POR UTILIZAR O NOSSO SISTEMA') + 4))
