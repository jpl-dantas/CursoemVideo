from math import sqrt
a = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
b = float(input('Agora digite o comprimento do cateto adjacente: '))
pa = a ** 2
pb = b ** 2
hi = pa + pb
hc = sqrt(hi)
print(f'O comprimento da hipotenusa é de {hc:.2f}')
