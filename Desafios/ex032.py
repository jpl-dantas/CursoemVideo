ano = int(input('Digite o ano que você queira: '))
abi = ano % 4
if abi and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
print(abi)
