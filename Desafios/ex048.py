print('A soma dos números ímpares multiplos de 3 que se encontram no intervalo de 1 a 500')
s = 0
if 500 % 2 == 0:
    for c in range(3, 500, 3):
        if c % 2 == 1:
            s = s + c
print(s)
