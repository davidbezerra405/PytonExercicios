altura = float(input('Informa a altura (em metros): '))
largura = float(input('Informe a largura (em metros): '))
area = altura * largura
print('altura = {:.3f} mt, largura = {:.3f}mt, área = {:.3f} m²'.format(altura, largura, area))
print('serão necessários {:.3f} litros de tinta para a pintura.'.format(area/2))
