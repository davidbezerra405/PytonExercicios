from datetime import date
anonasc = int(input('Informe o ano de nascimento: '))
anoatual = date.now().year
dif = anoatual - anonasc
if dif < 18:
    print('Ainda vai se alistar, falta {} ano(s)'.format(18 - dif))
elif dif > 18:
    print('Já passou {} ano(s) do tempo de se alistar'.format(dif - 18))
else:
    print('É hora de se alistar!')
