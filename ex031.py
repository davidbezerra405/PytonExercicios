kmr = int(input('Informe a distância da viagem em KM: '))
if kmr > 200:
    vlkm = 0.45
else:
    vlkm = 0.5
print('Você vai pagar R$ {:.2f} pela viagem.'.format(kmr * vlkm))
