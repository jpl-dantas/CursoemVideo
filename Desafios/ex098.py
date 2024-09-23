from time import sleep


# v Essa função recebe três parâmetros para criar um contador
# Com um início, fim e sequência da contagem.
def contador(i, f, c):
    if c > 0 and f < i:
        c *= -1
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if i > f and c > 0:
        c *= -1
    seq = c
    if seq < 0:
        seq = seq * -1
    print(f'Contagem de {i} até {f} de {seq} em {seq}:')
    sleep(1)
    for nu in range(i, f + c, c):
        print(f'{nu}', end=' > ')
        sleep(0.3)
    print('FIM')
    print('=' * 50)


# v Essa função é outro contador, porém ele é personalizado
# Onde o usuário decidirá os valores da contagem


contador(1, 10, 1)
contador(10, 1, -2)
print('Escreva os números para criar uma contagem:')
ini = int(input('Começo: '))
fim = int(input('Fim: '))
con = int(input('Sequência: '))
contador(ini, fim, con)
