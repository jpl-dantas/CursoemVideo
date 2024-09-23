n = int(input('Digite um número: '))
v = 1
s = n
res = ''
mep = n
maip = n
while res != 'NÃO' and res != 'N':
    v += 1
    on = int(input('Digite mais um número: '))
    if on > maip:
        maip = on
    if on < mep:
        mep = on
    s += on
    res = input('Você quer continuar digitando números? [S/N]: ').upper()
    if res != 'SIM' and res != 'S' and res != 'NÃO' and res != 'N':
        exit('Por favor, digite uma resposta válida.')
    print('-' * 45)
print(f'O maior número digitado foi: {maip}')
print(f'O menor número digitado foi: {mep}')
print(f'A média de todos os {v} números digitados é de {s / v:.1f}')
