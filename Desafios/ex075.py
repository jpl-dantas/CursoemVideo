n1 = int(input(f'Digite o 1º número: '))
n2 = int(input(f'Digite o 2º número: '))
n3 = int(input(f'Digite o 3º número: '))
n4 = int(input(f'Digite o 4º número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os números: {numeros}')
if numeros.count(9) > 1:
    es = 'es'
else:
    es = ''
if 9 in numeros:
    print(f'O número nove apareceu {numeros.count(9)} vez{es}')
else:
    print('Você não digitou o número nove nenhuma vez')

if 3 in numeros:
    print(f'O número três foi digitado na posição {numeros.index(3) + 1}')
else:
    print('O número três não foi digitado')

print('Os números pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
