n = int(input('Digite o número de início da contagem: '))
f = int(input('Digite o final da contagem: '))
s = int(input('Digite a sequência de contagem: '))
for contagem in range(n, f, s):
    print(contagem + 1, end=',')
