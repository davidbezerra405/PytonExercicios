valor = float(input('Qual o valor da casa? (R$) '))
sal = float(input('Qual o salário do comprador? (R$) '))
anos = int(input('Quantidade de anos para o pagamento? '))
vldisp = (sal * 30 / 100)
meses = (anos * 12)
vlmensal = (valor / meses)
print('Valor máximo a ser comprometido do salário (30%): R${:.2f}'.format(vldisp))
print('Valor da prestação mensal: R$ {:.2f}'.format(vlmensal))
if vlmensal > vldisp:
    print('empréstimo negado!')
else:
    print('empréstimo autorizado!')
