from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
r = 0
while r != 5:
    print('=' * 10, 'MENU', '=' * 10)
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Verificar qual é o maior\n'
          '[4] - Digitar novos números\n[5] - Sair do menu')
    print('=' * 26)
    r = int(input('Escolha uma opção: '))
    if r == 1:
        print(f'\033[32m{n1} + {n2} é = {n1 + n2}\033[m')
    elif r == 2:
        print(f'\033[32m{n1} x {n2} é = {n1 * n2}\033[m')
        sleep(3)
    elif r == 3:
        if n1 > n2:
            print(f'\033[32mO maior número entre {n1} e {n2} é {n1}\033[m')
        else:
            print(f'\033[32mO maior número entre {n1} e {n2} é {n2}\033[m')
    elif r == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
    elif r == 5:
        print('\033[36mFechando o menu...\033[m')
    else:
        print('\033[31mEscolha inválida, por favor escolha uma opção de 1 a 5.\033[m')
    sleep(3)
print('=' * 6, 'MENU FECHADO', '=' * 6)
