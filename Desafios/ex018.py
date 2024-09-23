import math
num = int(input('Digite um ângulo: '))
ang = math.radians(num)
sen = math.sin(ang)
cos = math.cos(ang)
tan = sen / cos
print(f'{num}° tem o valor de SENO de {sen:.2f}, COSSENO de {cos:.2f} e o TANGENTE de {tan:.2f}')
