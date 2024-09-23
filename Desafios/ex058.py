from random import randint
nc = randint(0, 10)
nt = 1
print('-' * 5, 'JOGO DA ADIVINHAÇÃO', '-' * 5)
nu = int(input('Digite um número de 0 a 10: '))
if nu == nc:
    print(f'\033[32mNÚMERO CORRETO\033[m\nParabéns você acertou o número na primeira tentativa')
else:
    while nc != nu:
        print('-' * 31)
        print('\033[31mNÚMERO ERRADO\033[m\nTente novamente.')
        nu = int(input('Digite um número de 0 a 10: '))
        nt += 1
        if nc == nu:
            print('-' * 31)
            print(f'\033[32mNÚMERO CORRETO\033[m\nVocê acertou na {nt}ª tentativa.')
