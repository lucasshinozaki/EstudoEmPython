nome = input('Digite seu nome completo : ')
nomesp = nome.split()
tamanho = len(nomesp) - 1

print('Nome {}, Sobrenome: {}'.format(nomesp[0], nomesp[tamanho]))
