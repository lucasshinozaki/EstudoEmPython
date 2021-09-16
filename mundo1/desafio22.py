nome = input("Digite seu nome completo: ")

print('Nome em maiusculo: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
print('Quantidade sem espaço: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(nome.split()[0])))
