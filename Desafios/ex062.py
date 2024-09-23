from time import sleep
print('=' * 5, 'Valor Aritimético', '=' * 5)
t = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite a sua razão: '))
v = 0
while v != 10:
    print(f'{t}', end=' -> ')
    v += 1
    t = t + r
print('FIM')
qa = 0
co = ''
while co != 'N':
    co = input('Você quer adicionar mais termos? [S/N]: ').upper()
    if co == 'S':
        qa = int(input('Quantos termos você deseja acidicionar?: '))
        tv = v + qa
        while v != tv:
            print(f'{t}', end=' -> ')
            v += 1
            t = t + r
        print('FIM')
    elif co == 'N':
        print('Fechando o programa...')
    else:
        print('\033[31mERRO. \nDigite S ou N.\033[m')
sleep(2.5)
print('Programa fechado.')
