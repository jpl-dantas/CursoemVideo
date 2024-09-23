print('=' * 5, 'Progressão Aritimética', '=' * 5)
print(' ' * 3, '10 Primeiros Valores')
print('=' * 29)
t = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite a sua razão: '))
v = 0
while v != 10:
    print(f'{t}', end=' -> ')
    v += 1
    t = t + r
print('FIM')
