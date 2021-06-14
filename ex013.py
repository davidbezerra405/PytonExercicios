salario = float(input('Salário atual (R$): '))
aumento = float(input('Aumento (%): '))
acrescimo = salario+(salario*aumento/100)
print('Novo Salario R$ {:.2f}'.format(acrescimo))
