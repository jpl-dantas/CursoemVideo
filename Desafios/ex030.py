nmr = int(input('Digite um número para saber se ele é par ou ímpar: '))
cal = nmr % 2
if cal == 0:
    print(f'O número {nmr} é par.')
else:
    print(f'O número {nmr} é ímpar')
