tabela = ('Bragantino', 'Athletico-PR', 'Fortaleza', 'Bahia', 'Palmeiras', 'Atlético-GO', 'Atlétio-MG',
          'Flamengo', 'Fluminense', 'Juventude', 'Santos', 'Corinthians', 'Ceará SC', 'Internacional',
          'Sport Recife', 'Cuiabá', 'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')
print('5 primeiros colocados')
print('-'*21)
print(tabela[:5])
for pos in range(0, 5):
    print(f'{pos+1} - {tabela[pos]}')
print('')

print('4 últimos colocados')
print(tabela[-4:])
for pos in range(len(tabela) - 4, len(tabela)):
    print(f'{pos + 1} - {tabela[pos]}')
print('')

print('Em ordem alfabética')
print(sorted(tabela))
tabelaalfa = sorted(tabela)
for time in tabelaalfa:
    print(time)
print('')

print(f'O Chapecoense esta na posição {tabela.index("Chapecoense")+1}')
print('\nFim')
