n = 0
v = 0
s = 0
while n <= 999:
    s += n
    n = int(input('Digite um número: '))
    v += 1
print(f'A soma total de todos os números digitados é {s}')
print(f'O total de números digitados foi de {v}')
