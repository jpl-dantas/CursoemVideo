print('=' * 43)
CM = ' CHEAP MARKET '
print(f'{CM:-^43}')
print('=' * 43)
np = r = 'S'
pre = mil = tot = cme = mep = 0
nup = 1
nmp = ''
while True:
    r = input(f'Você quer adicionar um {nup}º produto? [S/N]: ').upper()
    if r == 'N':
        break
    elif r == 'S':
        np = input('Nome do produto: ')
        pre = float(input('Preço do produto: R$'))
        if pre < 0.01:
            print('\033[31m-> Digite um preço válido\033[m')
        else:
            nup += 1
            tot += pre
            if pre > 1000:
                mil += 1
            if cme == 0:
                mep = pre
                nmp = np
            else:
                if pre < mep:
                    mep = pre
                    nmp = np
            cme += 1
            print('=' * 43)
    else:
        print('\033[31m-> Escolha uma opção correta (S ou N)\033[m')
print('=' * 43)
if nup > 1:
    if mil > 1:
        em = 'em'
        s = 's'
    else:
        em = 'e'
        s = ''
    print(f'Total gasto: R${tot}')
    if mil >= 1:
        print(f'Exist{em} {mil} produto{s} que val{em} mais de 1000 reais.')
    else:
        print('Nenhum produto custou mais de mil reais')
    if nup <= 2:
        print(f'O produto mais barato comprado foi óbviamente\no único que você comprou.\n'
              f'-> {nmp}, valendo R${mep}')
    else:
        print(f'O produto mais barato comprado foi:\n-> {nmp}, valendo R${mep}')
    print('=' * 43)
else:
    print('Você não adicionou nenhum produto\nno seu carrinho de compras.')
