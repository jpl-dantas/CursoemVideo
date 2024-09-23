r1 = float(input('Digite o comprimento da reta inclinada: '))
r2 = float(input('Digite o comprimento da reta vertical: '))
r3 = float(input('Digite o comprimento da reta horizontal: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível criar um triangulo.')
else:
    print('Não é possível criar um triangulo.')
