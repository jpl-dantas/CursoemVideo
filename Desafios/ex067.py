from time import sleep
n = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n <= -1:
        break
    print('=' * 7, 'TABUADA', '=' * 7)
    ve = 0
    while ve != 10:
        ve += 1
        print(f'{n} x {ve} = {n * ve}')
    print('=' * 23)
    sleep(1.5)
print('=' * 23)
print('-> Fechando a tabuada...')
sleep(3)
print('-> Tabuada fechada.')
