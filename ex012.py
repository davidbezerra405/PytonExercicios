preco = float(input('Preço do produto (R$): '))
desconto = float(input('Desconto (%): '))
venda = preco-(preco*desconto/100)
print('Preço com desconto R$ {:.2f}'.format(venda))