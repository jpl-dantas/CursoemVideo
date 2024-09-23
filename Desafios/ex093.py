dados = {
    'nome': input('Nome do jogador: '),
    'número de jogos do jogador': int(input('Jogos jogados: '))
}
print('=' * 45)

total = 0
if dados['número de jogos do jogador'] >= 1:
    dados['gols'] = []
    for rep in range(1, dados['número de jogos do jogador'] + 1):
        dados['gols'].append(int(input(f'Gols feitos na {rep}ª partida: ')))
        total += dados['gols'][rep - 1]
    dados['total'] = total
    print('=' * 45)

    print(dados)
    print('=' * 45)

    for k, v in dados.items():
        print(f'{k}: {v}')
    print('=' * 45)

    print(f'{dados["nome"]} jogou {dados["número de jogos do jogador"]} partidas.')
    for rep in range(1, dados['número de jogos do jogador'] + 1):
        print(f'    - Na {rep}ª partida ele fez {dados["gols"][rep - 1]} gols.')
    print(f'No total foram {dados["total"]} gols.')
else:
    print(f'{dados["nome"]} não jogou nenhuma partida.')
