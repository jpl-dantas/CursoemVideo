print('Digite abaixo o comprimento das retas para conferir se é possível criar um triângulo.')
r1 = float(input('Digite o comprimento da reta inclinada: '))
r2 = float(input('Digite o comprimento da reta vertical: '))
r3 = float(input('Digite o comprimento da reta horizontal: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível criar um triangulo ', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 != r2 != r3:
        print('isósceles.')
    else:
        print('escaleno.')
else:
    print('Não é possível criar um triangulo.')
