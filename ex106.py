from time import sleep


def cor(nome='normal'):
    r = '\033[m'
    if nome == 'fundoverde':
        r = '\033[0;30;42m'
    elif nome == 'fundoazul':
        r = '\033[0;30;44m'
    elif nome == 'fundobranco':
        r = '\033[7m'
    elif nome == 'fundorosa':
        r = '\033[0;30;45m'
    return r


def cab(msg, corf=''):
    t = len(msg)+4
    cf = cor(corf)
    print(cf, '-'*t)
    print(cf, '  '+msg+'  ')
    print(cf, '-'*t)
    print(cor(), end='')


while True:
    cab('SISTEMA DE AJUDA PyHELP', 'fundoverde')
    fbhelp = str(input('Função ou Biblioteca > ')).strip()
    if fbhelp.upper() == 'FIM':
        break
    cab(f'Acessando o manual do comando \'{fbhelp}\'', 'fundoazul')
    sleep(0.5)
    print(cor('fundobranco'), end='')
    help(fbhelp)
    sleep(2)
cab('ATÉ LOGO', 'fundorosa')
