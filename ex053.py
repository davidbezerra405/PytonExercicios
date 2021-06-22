palavra = str(input('Digie uma frase: ')).strip()
palavra = palavra.upper().replace(" ", "")
palidromo = ''
tamanho = len(palavra)
for c in range(tamanho-1, -1, -1):
    palidromo = palidromo + palavra[c]
print(palidromo)
if palidromo == palavra:
    print('A frase é um PALÍDROMO')
else:
    print('A frase NÃO é um palídromo')
