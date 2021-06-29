from datetime import datetime
anoatual = datetime.now().year
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
anonasc = int(input('Ano de Nascimento: '))
aluno['idade'] = anoatual - anonasc
aluno['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if aluno['ctps'] != 0:
    aluno['contratação'] = int(input('Ano de contratação: '))
    aluno['salário'] = float(input('Salário: R$ '))
    aluno['aposentadoria'] = aluno['idade'] + (35 - (anoatual - aluno['contratação']))
print('-'*40)
for k, v in aluno.items():
    print(f'{k} tem o valor {v}')
