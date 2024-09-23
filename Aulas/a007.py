n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
su = n1 - n2
d = n1 / n2
m = n1 * n2
print(f'A soma entre {n1} + {n2} é igual a: {s}', end='')
print(f', a subtração entre {n1} - {n2} é igual a: {su}', end='')
print(f', a divisão entre {n1} / {n2} é igual a: {d:.3f}', end=' ')
print(f'e a multiplicação entre {n1} x {n2} é igual a: {m}')