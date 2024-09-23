n = float(input('Digite o preço do seu produto: R$'))
d = int(input('Quantos porcento de desconto você deseja? '))
ds = d / 100
dc = ds * n
pc = n - dc
print(f'O valor do produto é {n}, com o desconto de {d}% o preço cai para R${pc:.2f}.')
