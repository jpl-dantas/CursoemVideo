print('=' * 43)
BST = ' BANCO FASTPAY'
print(f'{BST:-^43}')
print('=' * 43)

n = int(input('Quanto você deseja sacar?: '))
if n >= 1:
    ce50 = ce20 = ce10 = m1 = saque = 0
    if n >= 50:
        ce50 = (n - saque) // 50
        saque += 50 * ce50
    if n >= 20:
        ce20 = (n - saque) // 20
        saque += 20 * ce20
    if n >= 10:
        ce10 = (n - saque) // 10
        saque += 10 * ce10
    if n >= 1:
        m1 = (n - saque) // 1
        saque += 1 * m1

    print('\033[4mTotal Sacado\033[m:')

    if ce50 >= 1:
        if ce50 >= 2:
            s = 's'
        else:
            s = ''
        print(f'-> {ce50} cédula{s} de R$50')
    if ce20 >= 1:
        if ce20 >= 2:
            s = 's'
        else:
            s = ''
        print(f'-> {ce20} cédula{s} de R$20')
    if ce10 >= 1:
        if ce10 >= 2:
            s = 's'
        else:
            s = ''
        print(f'-> {ce10} cédula{s} de R$10')
    if m1 >= 1:
        if m1 >= 2:
            s = 's'
        else:
            s = ''
        print(f'-> {m1} moeda{s} de R$1')
    print('=' * 43)
    print('VOLTE SEMPRE NA BANCO FASTPAY!')
else:
    print('NÚMERO INVÁLIDO PARA SAQUE.')
