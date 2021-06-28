expressao = str(input('Digite uma expressão: '))
abrep = 0
fechap = 0
for d in expressao:
    if d == '(':
        abrep += 1
    elif d == ')':
        fechap += 1
if abrep == fechap:
    print('Sua expressão está correta!')
else:
    print('Sua expressão esta errada!')
