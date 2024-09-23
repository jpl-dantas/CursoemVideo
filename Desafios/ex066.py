n = s = cn = 0
while True:
    n = int(input('Digite um número (999 to stop): '))
    if n >= 999:
        break
    s += n
    cn += 1
print(f'A soma dos {cn} valores é: {s}')
