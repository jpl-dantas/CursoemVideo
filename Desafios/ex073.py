from time import sleep
times = ('BOTAFOGO', 'RED BULL BRAGANTINO', 'GRÊMIO', 'PALMEIRAS', 'FLAMENGO', 'FLUMINENSE', 'ATLÉTICO-MG',
         'ATHLETICO-PR', 'FORTALEZA', 'SÃO PAULO', 'CUIABÁ', 'CRUZEIRO', 'CORINTHIANS', 'INTERNACIONAL', 'SANTOS',
         'GOIÁS', 'VASCO', 'BAHIA', 'AMÉRICA-MG', 'CORITIBA')
print('=' * 58)
print('Os primeiros 5 times colocados do Brasileirão Série A são: ')
print('=' * 58)
sleep(3)

for pricolo in range(0, len(times[0:5])):
    print(f'{pricolo + 1}º - {times[pricolo]}')
print('=' * 58)
sleep(1.5)

print('Os últimos 4 colocados da tabela são: ')
print('=' * 58)
sleep(3)

pos = 17
for ultcolo in range(-4, len(times[-1: -4])):
    print(f'{pos}º - {times[ultcolo]}')
    pos += 1
print('=' * 58)
sleep(1.5)

print('Lista dos nomes dos times em ordem alfabéitca:')
print('=' * 58)
sleep(3)

timalf = sorted(times)
for ordalf in range(0, len(timalf)):
    print(f'{timalf[ordalf][0]} - {timalf[ordalf]}')
print('=' * 58)
sleep(1.5)

print('Posição do São Paulo na tabela:')
print('=' * 58)
sleep(3)

print(f'{times.index("SÃO PAULO") + 1}ª Colocação')
