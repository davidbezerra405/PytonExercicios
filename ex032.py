from datetime import date
ano = int(input('Informe o ano: '))
if ano == 0:
    ano = date.today().year
print('Ano: {}'.format(ano))
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano bissexto')
