n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('=' * 3, 'TABUADA', '=' * 3)
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
print('=' * 14)
