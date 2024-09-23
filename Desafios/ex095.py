from time import sleep

jogadores = []
while True:
    dados = {
        'nome': input('Nome do jogador: '),
        'número de jogos do jogador': ''
    }

    total = 0
    while True:
        njj = int(input('Partidas jogadas [MAX = 5]: '))
        if njj > 5 or njj < 1:
            print('\033[31m| Quantidade de jogos inválida.\033[m')
            print('-=' * 22)
        else:
            dados['número de jogos do jogador'] = njj
            break
    if dados['número de jogos do jogador'] >= 1:
        dados['gols'] = []
        for rep in range(1, dados['número de jogos do jogador'] + 1):
            dados['gols'].append(int(input(f'Gols feitos na {rep}ª partida: ')))
            total += dados['gols'][rep - 1]
        dados['total'] = total
        jogadores.append(dados.copy())
        print('-' * 44)
    while True:
        r = input('Você quer adicionar mais pessoas? [S/N]: ').upper()
        if r == 'N' or r == 'S':
            break
        else:
            print('\033[31m| Por favor digite uma resposta válida\033[m')
            print('-=' * 22)
    if r == 'N':
        break

print('=' * 60)
print(f'|{" Nº | NOME": <33}| {"GOLS": <16}| {"TOTAL": <7}')
print('-' * 60)
p = 0
for j in jogadores:
    print(f'|{p: ^4}| {j["nome"]: <27}| {str(j["gols"]): <16}| {j["total"]: <7}')
    p += 1
    sleep(0.8)
print('=' * 60)

re = 'S'
nu = 0
quer = 'deseja'
az = 'algum'
seq = 0
while True:
    while True:
        if seq > 0:
            az = 'mais algum'
            quer = 'ainda deseja'
        re = input(f'Você {quer} ver os dados detalhados de {az} jogador? [S/N]: ').upper()
        if re == 'N' or re == 'S':
            break
        else:
            print('\033[31m| Por favor digite uma resposta válida\033[m')
            print('=-=' * 19)
    if re == 'N':
        sleep(1)
        print('| Obrigado por usar o nosso sitema de registro de partidas.')
        sleep(1)
        print('| Tenha um ótimo dia.')
        sleep(0.8)
        print('=' * 60)
        break

    while True:
        joga = int(input('Qual é o Nº do jogador? '))
        if joga > len(jogadores) - 1 or joga < 0:
            print('\033[31m| Não existe nenhum jogador com esse número. \n| Tente novamente.\033[m')
            print('=-=' * 19)
        else:
            print('-' * 60)
            print(f'-> Levantamento do jogador {jogadores[joga]["nome"]}')
            sleep(1)
            part = 1
            for jogo in jogadores[joga]['gols']:
                print(f'    Na {part}ª partida o jogador fez {jogo} gol(s).')
                sleep(0.5)
                part += 1
            print('-' * 60)
            seq += 1
            break
