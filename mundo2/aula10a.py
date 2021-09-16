nome = str(input('Qual é seu nome ? ')).strip()

if nome == 'Lucas':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))
