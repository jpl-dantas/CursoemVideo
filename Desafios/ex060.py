from math import factorial
n = int(input('Digite um número: '))
nr = n
nc = n
f = factorial(n)
r = input('For, While ou math.factorial? [F/W/MF]: ').upper()
if r == 'W':
    print(f'{n}! = ', end='')
    while nr != 1:
        print(nr, end=' x ')
        nr -= 1
        nc = nr * nc
    print('1 =', nc)
elif r == 'F':
    print(f'{n}! = {n} x ', end='')
    for c in range(n - 1, 1, -1):
        print(c, end=' x ')
        nc = nc * c
    print('1 =', nc)
elif r == 'MF':
    print(f'O fatorial de {n}! é {f}')
else:
    print('\033[31mPor favor, escolha uma opção correta da próxima vez.')
