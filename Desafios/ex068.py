from random import randint
from time import sleep
n = v = 0
r = ''
pa1 = ' ÍMPAR OU PAR '
mpi = 0
print('=' * 35)
print(f'{pa1:-^35}')
print('=' * 35)
while True:
    mpi = randint(1, 10)
    r = input('Ímpar ou Par? [I/P]: ').upper()
    if r != 'I' and r != 'P':
        print('\033[31mPor favor, digite I ou P.\033[m')
        sleep(1.5)
        break
    n = int(input('Escolha um número de 1 a 10: '))
    if n > 10 or n < 0:
        print('\033[31mPor favor, digite um número de 1 a 10.\033[m')
        sleep(1.5)
    if r == 'I' and n <= 10 and n >= 0:
        if (n + mpi) % 2 == 0:
            print(f'Você digitou {n} e a máquina digitou {mpi}.')
            sleep(0.5)
            print(f'{n} + {mpi} é: {n + mpi} que é \033[31mPar\033[m. Você perdeu.')
            sleep(1.5)
            break
        else:
            print(f'Você digitou {n} e a máquina digitou {mpi}.')
            sleep(0.5)
            print(f'{n} + {mpi} é: {n + mpi} que é \033[32mÍmpar\033[m. Você venceu!.')
            v += 1
    elif r == 'P' and n <= 10 and n >= 0:
        if (n + mpi) % 2 == 0:
            print(f'Você digitou {n} e a máquina digitou {mpi}.')
            sleep(0.5)
            print(f'{n} + {mpi} é: {n + mpi} que é \033[32mPar\033[m. Você venceu.')
            v += 1
        else:
            print(f'Você digitou {n} e a máquina digitou {mpi}.')
            sleep(2)
            print(f'{n} + {mpi} é: {n + mpi} que é \033[31mÍmpar\033[m. Você perdeu.')
            sleep(1.5)
            break
    sleep(1.5)
print('=' * 35)
if v > 1:
    s = 'es'
    con = ' consecutivas'
else:
    s = ''
    con = ''
if v >= 1:
    print(f'Você venceu {v} vez{s}{con}. Parábens!')
elif v == 0 and r == 'I' or r == 'P':
    print('Você não venceu nenhuma vez \nque falta de sorte! Tente novamente!')
if r != 'I' and r != 'P':
    print('\033[1:31mDigite uma opção correta da próxima vez.\033[m')
