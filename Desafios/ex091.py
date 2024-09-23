from random import randint
from time import sleep

jogadores = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
print('Valores sorteados: ')
for e in jogadores.keys():
    jogadores[e] = randint(1, 6)
    sleep(0.8)
    print(f'    O {e} sorteou o número {jogadores[e]}')

print('Ranking dos jogadores: ')
for r in range(1, 5):
    for e in jogadores.keys():
        if jogadores[e] == max(jogadores.values()):
            sleep(0.8)
            print(f'    {r}º lugar: {e} que tirou {jogadores[e]}')
            del jogadores[e]
            break
