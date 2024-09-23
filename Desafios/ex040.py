print('Digite o valor das suas duas notas abaixo:')
pn = float(input('Primeira nota: '))
sn = float(input('Segunda nota: '))
m = (pn + sn) / 2
print(f'A média das suas notas é {m}')
if m <= 4.9:
    print('\033[31mVocê foi reprovado\033[m')
elif 5 <= m <= 6.9:
    print('\033[33mVocê esta de recuperação.\033[m')
elif m >= 7:
    print('\033[32mVocê passou no teste.\033[m')
