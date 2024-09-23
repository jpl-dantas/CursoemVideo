from time import sleep

dados = [[], []]
print('=' * 45)
print(f'{"REGISTRO BOLETIM ESCOLAR": ^45}')
print('=' * 45)

r = ''
seq = 0
while True:
    dados[0].append(input('Nome do aluno: '))
    while True:
        nota1 = float(input('Primeira nota do aluno: '))
        if nota1 >= 0 and nota1 <= 10:
            dados[1].append([])
            dados[1][seq].append(nota1)
            break
        else:
            print('\033[31m| Digite uma nota válida [0 - 10]\033[m')
            print('=' * 45)
    while True:
        nota2 = float(input('Segunda nota do aluno: '))
        if nota2 >= 0 and nota2 <= 10:
            dados[1][seq].append(nota2)
            break
        else:
            print('\033[31m| Digite uma nota válida [0 - 10]\033[m')
            print('=' * 45)
    seq += 1

    while r != 'S' and r != 'N':
        r = input('Você quer adicionar mais alunos? [S/N]: ').upper()
        if r == 'N' or r == 'S':
            break
        else:
            print('\033[31m| Por favor digite uma resposta válida\033[m')
    if r == 'N':
        print('=' * 45)
        break
    r = ''
    print('=' * 45)

print(f'|{" Nº | NOME": <33}|{"MÉDIA": ^9}|')
print('-' * 45)

for n in dados[0]:
    media = (dados[1][dados[0].index(n)][0] + dados[1][dados[0].index(n)][1]) / 2
    print(f'|{dados[0].index(n): ^4}| {n: <27}|{media: ^9}|')
    sleep(0.8)
print('=' * 45)

re = 'S'
nu = 0
quer = 'quer'
az = 'as'
seq = 0
while True:
    while True:
        if seq > 0:
            az = 'outras'
            quer = 'ainda quer'
        re = input(f'Você {quer} ver {az} notas dos alunos? [S/N]: ').upper()
        if re == 'N' or re == 'S':
            break
        else:
            print('\033[31m| Por favor digite uma resposta válida\033[m')
            print('=' * 45)
    if re == 'N':
        sleep(1)
        print('| Obrigado por usar o nosso \n  sitema de boletim escolar.')
        sleep(1)
        print('| Tenha um ótimo dia.')
        sleep(0.8)
        print('=-=' * 15)
        break

    while True:
        nu = int(input('Você deseja mostrar as notas de qual aluno? [Nº]: '))
        if nu > len(dados[0]) - 1 or nu < 0:
            print(f'\033[31m| O aluno número {nu} infelizmente não foi encontrado. | Tente outro número.\033[m')
            print('=' * 45)
        else:
            print(f'| {dados[0][nu]} tirou {dados[1][nu][0]} e {dados[1][nu][1]} |')
            sleep(1)
            print(f'=' * 45)
            break
    seq += 1
