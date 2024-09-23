from time import sleep
from random import randint
numeros = []


def sorteia(lista):
    """Essa função serve para sortear 5 números aleatórios de 0 a

        :param lista:  O parâmetro lista serve para você colocar o nome da lista que você deseja sortear 5 números.
        :return: sem retorno
        """

    print(f'Adicionando 5 números aleatórios na sua lista...')
    sleep(1)
    for rep in range(0, 5):
        numt = randint(0, 100)
        print(numt, end=' ')
        sleep(0.5)
        lista.append(numt)
    print('PRONTO!')


def somapar(lista):
    sp = 0
    for n in lista:
        if n % 2 == 0:
            sp += n
    print(f'A soma dos números pares da lista {lista} é {sp}')


sorteia(numeros)
somapar(numeros)
print(sorteia.__doc__)
