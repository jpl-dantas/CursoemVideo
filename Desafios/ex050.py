s = 0
for c in range(1, 7):
    v = int(input(f'Digite o {c}º valor inteiro: '))
    if v % 2 == 0:
        s = s + v
if s == 0:
    print('Você digitou apenas números ímpares.')
else:
    print(f'A soma de todos os números pares que você digitou é {s}.')
