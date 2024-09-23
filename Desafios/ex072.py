numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre \033[31m0 e 20\033[m: '))
while n < 0 or n > 20:
    n = int(input('\033[31mNúmero incorreto\033[m | Tente novamente: '))

print(f'Você digitou o número {numeros[n]}')
