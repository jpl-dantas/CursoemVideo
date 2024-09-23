from random import randint
from time import sleep

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = {}

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(0.8)
    print(f'    O {k} sorteou o número {v}')

pos = 1
ranking = sorted(jogadores.items(), key=lambda value: value[1], reverse=True)
print('Ranking jogadores:')
for k, v in ranking:
    sleep(0.8)
    print(f'    {pos}º lugar: {k} com {v} pontos')
    pos += 1
