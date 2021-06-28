itens = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*31)
print(f'{"LISTAGEM DE PREÇOS":^31}')
print('-'*31)
for pos in range(0, len(itens), 2):
    print(f'{itens[pos]:.<20}R$ {itens[pos+1]:>8.2f}')
print('-'*31)