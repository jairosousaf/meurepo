# Em qual turno você estuda?
turno = input(f'Digite seu turno de trabalho: M para Matutino, V para Vespertino e N para Noturno. ')

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido!')