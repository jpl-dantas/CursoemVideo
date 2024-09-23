def futstatics(n, g):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if not n:
        n = '<desconhecido>'
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


print('-' * 30)
jogador = input('Nome do jogador: ')
gols = input('Gols feitos pelo jogador: ')
print(futstatics(jogador, gols))
