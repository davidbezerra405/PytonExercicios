qnt = total = qntmaismil = menorpreco = 0
descmenorpreco = ''
print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)
while True:
    print(f'Produto {qnt+1}')
    desc = str(input('Descrição: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    qnt += 1
    total += preco
    if preco > 1000.0:
        qntmaismil += 1
    if (qnt == 1) or (preco < menorpreco):
        menorpreco = preco
        descmenorpreco = desc
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {qntmaismil} produto(s) custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {descmenorpreco} que custa R$ {menorpreco:.2f}')
