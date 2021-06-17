num = str(input('Informe um número entre 0 e 9999: ')).strip()
print('O número informado tem {} digito(s).'.format(len(num)))
numint = int(num)
print('')

#print('String')
#print('-'*10)
#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))

print('')
print('Inteiro')
print('-'*10)
#numm = int((numint - numint % 1000) / 1000)
#numint = int(numint % 1000)
#numc = int((numint - numint % 100) / 100)
#numint = int(numint % 100)
#numd = int((numint - numint % 10) / 10)
#numint = int(numint % 10)
#numu = int((numint - numint % 1))

numu = numint // 1 % 10
numd = numint // 10 % 10
numc = numint // 100 % 10
numm = numint // 1000 % 10

print('Unidade: {}'.format(numu))
print('Dezena: {}'.format(numd))
print('Centena: {}'.format(numc))
print('Milhar: {}'.format(numm))

