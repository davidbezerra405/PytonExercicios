nomecidade = str(input('Digite o nome da sua cidade: ')).strip()
print('Sua cidade começa com SANTO? {}'.format('santo' in nomecidade.split()[0].lower()))
