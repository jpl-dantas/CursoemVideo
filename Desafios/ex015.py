km = float(input('Quantos km seu carro rodou? '))
dias = int(input('Quantos dias você utilizou o carro? '))
pkm = km * 0.15
pdia = dias * 60
valor = pkm + pdia
print(f'Como seu carro rodou {km}Km enquanto você o utilizava por {dias} dia(s), o preço a pagar para a locadora de '
      f'carros será de R${valor:.2f}. \nR${pkm:.2f} pelos quilômetros rodados e R${pdia} pelos dia(s) com o carro.')
