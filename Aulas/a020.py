def linig():
    print('=' * 20)


def lintr():
    print('-' * 20)


linig()
print(f'{"PYTHON": ^20}')
lintr()


def saudacao(nome):
    print(f'Saudações, {nome}.')


saudacao('João')


def soma(a, b):
    print(f'{a} + {b} = {a + b}')


soma(1, 5)


def soma(a, b):
    print(f'{a}(A) + {b}(B) = {a + b}')


soma(b=11, a=9)
soma(11, 9)
