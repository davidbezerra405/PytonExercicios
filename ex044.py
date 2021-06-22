print('{:=^40}'.format(' LOJA DO ZÉ '))
preco = float(input('Preço normal: (R$) '))
print('Condições de pagamento:')
print('1-Á vista (dinheiro/cheque) desconto -10%')
print('2-Á vista (cartão) desconto -5%')
print('3-Em até 2x (cartão) preço normal ')
print('4-3x ou mais (cartão) acréscimo +20%')
op = int(input('Escolha: '))
valor = 0.0
if op == 1:
    valor = preco - (preco * 10 / 100)
elif op == 2:
    valor = preco - (preco * 5 / 100)
elif op == 3:
    valor = preco
elif op == 4:
    valor = preco + (preco * 20 / 100)
else:
    print('Opção invalida!')
if valor > 0.0:
    print('Valor a ser pago = R$ {:.2f}'.format(valor))
