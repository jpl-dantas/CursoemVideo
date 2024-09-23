n = int(input('Quantos termos você quer mostrar? '))
rep = 0
t1 = 0
t2 = 1
sm = 0
print(f'{t1} -> {t2}', end=' -> ')
while rep != n:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    rep += 1
print('FIM')
