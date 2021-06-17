v = int(input('Informe a velocidade do carro: '))
if v > 80:
    e = v - 80
    m = e * 7.0
    print('Voce passou {}km/h acima do limite de 80km/h\nFoi multado em R$ {:.2f}\nMelhor chegar atrasado que de carona no rabecao!'.format(e, m))
else:
    print('Cara responsavel!')
