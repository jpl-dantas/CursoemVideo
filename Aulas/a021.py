from time import sleep


def linha(crt, qnt):
    """
    -> Essa função retorna uma linha com o tamanho desejado de um caractere específico
    :param crt: caractere
    :param qnt: quantidade de caracteres
    :return: sem retorno
    """
    # ^ docstring ^

    print(f'{crt}' * qnt)


# Interactive Help
print('\033[33mInteractive Help\033[m')
sleep(2)

help(print)
print('-' * 50)
sleep(5)
help(linha)
print('-' * 50)
sleep(5)
help()  # Escreva 'quit' para sair
print('=' * 50)

# docstrings
print('\033[33mdocstrings\033[m')
sleep(2)

print(print.__doc__)
print('-' * 50)
print(linha.__doc__)
print('=' * 50)
sleep(5)

# Parâmetros opcionais
print('\033[33mParâmetros opcionais\033[m')
sleep(2)


def soma(a=0, b=0, c=0):
    s = a + b + c
    print(s)


soma(5)
soma(1, 2)
soma()
print('=' * 50)
sleep(5)

# Escopo de Variável Local
print('\033[33mEscopo de Variável Local\033[m')
sleep(2)


def minha_funcao():
    x = 10  # x é uma variável local
    print(x)


minha_funcao()  # Saída: 10
# print(x)  # Isso resultaria em um erro, pois x é uma variável local e não está acessível fora da função.
print('=' * 50)
sleep(5)

# Escopo de Variável Global
print('\033[33mEscopo de Variável Global\033[m')
y = 20  # y é uma variável global
sleep(2)


def minha_funcao2():
    global y
    y = 30  # Modificando a variável global y
    print(y)


minha_funcao2()  # Saída: 30
print('-' * 50)
print(y)  # Saída: 30, pois y foi modificado dentro da função
print('=' * 50)
sleep(5)

# Retornando Valores
print('\033[33mRetornando Valores\033[m')


def soma(a, b):
    return a + b


resultado = soma(3, 4)
print(resultado)  # Saída: 7
