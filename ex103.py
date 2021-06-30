def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconehcido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


jogador = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: ')).strip()
print(ficha(jogador, gols))
