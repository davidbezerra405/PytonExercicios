def área(l, c):
    a = l * c
    print(f'A área de um terrono {l:.1f}x{c:.1f} e de {a:.1f}m².')


def cab(txt):
    t = len(txt)+4
    c = (t - len(txt)) // 2 -1
    print('-'*t)
    print(' '*c,f'{txt}')
    print('-'*t)


cab('Controle de Terrenos - Python 3.0')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
