def voto(ano):
    from datetime import date
    anoa = date.today().year
    idade = anoa - ano
    if idade < 16:
        return f'Com {idade} anos: SEM DIREITO A VOTO'
    elif idade >= 50 or idade <= 17 and idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

