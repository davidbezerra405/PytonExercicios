d = int(input('Quantidade dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (d * 60) + (km * 0.15)
print('O total a pagar e de R${:.2f}'.format(valor))
