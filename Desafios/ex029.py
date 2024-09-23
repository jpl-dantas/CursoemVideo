import emoji
km = int(input('Digite quantos km/h seu carro estava quando ultrapassou o radar de velocidade: Km/h '))
if km >= 81:
    multa = (km - 80) * 7.0
    print(f'Você ultrapassou o limite de velocidade e recebeu uma multa de R${multa}')
else:
    print(emoji.emojize('Você não ultrapassou o limite de velocidade.'))
