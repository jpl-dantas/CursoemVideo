from random import randint
from time import sleep

print('-' * 37)
print(f'{"LUCKY SENA": ^37}')
print('-' * 37)

rep = int(input('Quantos jogos você deseja sortear? '))
jogos = []
nrep = 0
S10J = f' Sorteado {rep} Jogos '
if rep >= 1:
    print(f'{S10J:=^37}')
    for vez in range(0, rep):
        jogos.append([])
        for i in range(0, 6):
            while True:
                n = randint(1, 60)
                if n not in jogos[nrep]:
                    jogos[nrep].append(n)
                    break
        sleep(0.8)
        print(f'{vez + 1}º Jogo: {sorted(jogos[nrep])}')
        nrep += 1
    sleep(0.5)
    print('=' * 37)
    sleep(1)
    print(f'{" COM A LUCKY SENA ":-^37}')
    sleep(1)
    print(f'{" VOCÊ SEMPRE TEM SORTE ":-^37}')
    sleep(0.5)
    print(f'=' * 37)
else:
    print('Você não quis sortear nem um jogo.')
