def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if idade < 16:
        situacao = f'Com {idade} anos: Voto NEGADO!'
    elif (16 <= idade < 18) or idade >= 65:
        situacao = f'Com {idade} anos: Voto OPCIONAL'
    else:
        situacao = f'Com {idade} anos: Voto OBRIGATÓRIO'
    return situacao


anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))
