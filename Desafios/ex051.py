print('=' * 5, 'Valor Aritimético', '=' * 5)
print(' ' * 3, '10 Primeiros Valores')
print('=' * 29)
t = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite a sua razão: '))
d = t + (10 - 1) * r
for c2 in range(t, d + r, r):
    print(f'{c2}', end=' -> ')
print('FIM')
