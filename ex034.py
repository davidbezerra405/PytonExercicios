sal = float(input('Informe o sálario: '))
if sal > 1250.0:
    perc = 10
else:
    perc = 15
aumento = sal * perc / 100
print('Seu sálario é R$ {:.2f}\nTeve um aumento de {:.2f}%\nValor do Aumento R$ {:.2f}\nSálario atual R$ {:.2f}'.format(sal, perc, aumento, (sal+aumento)))
