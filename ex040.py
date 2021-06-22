nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
media = (nota1 + nota2) / 2
print('Média: {:.1f} - '.format(media), end='')
if media < 5.0:
    print('Aluno REPROVADO!')
elif 5.0 <= media <= 6.9:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')
