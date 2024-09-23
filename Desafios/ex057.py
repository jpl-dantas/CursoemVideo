sexo = input('Qual é seu sexo? [M/F]: ').upper()
if sexo == 'M' or sexo == 'F':
    print('Fim')
else:
    while sexo != 'M' and sexo != 'F':
        sexo = input('Opção inválida. Informe corretamente qual é o seu sexo:  ').upper()
    print('Fim')
