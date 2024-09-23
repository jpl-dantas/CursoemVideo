dist = float(input('Digite em quilômetros a distância total do percurso da sua viagem: '))
if dist <= 199:
    vap = dist * 0.50
    print(f'O valor a pagar pela viagem será de: R${vap}')
if dist >= 200:
    vap = dist * 0.45
    print(f'O valor a pagar pela viagem será de: R${vap}')
