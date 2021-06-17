n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
nme = n1
nma = n1
if nme > n2:
    nme = n2
if nme > n3:
    nme = n3
if nma < n2:
    nma = n2
if nma < n3:
    nma = n3
print('O menor número é {} e o menor é {}'.format(nme, nma))
