import random

print('Escolha: pedra, papel ou tesoura')
escolha = input('Escolha uma das opções: ')

aleatorio = ['pedra', 'tesoura', 'papel']
random.shuffle(aleatorio)

if aleatorio[0] == escolha:
    print('EMPATE\nSUA ESCOLHA: {}\nESCOLHA DO COMPUTADOR: {}\n'.format(escolha, aleatorio[0]))
elif aleatorio[0] == 'tesoura' and escolha == 'pedra':
    print('GANHOU\nSUA ESCOLHA: {}\nESCOLHA DO COMPUTADOR: {}\n'.format(escolha, aleatorio[0]))
elif aleatorio[0] == 'papel' and escolha == 'tesoura':
    print('GANHOU\nSUA ESCOLHA: {}\nESCOLHA DO COMPUTADOR: {}\n'.format(escolha, aleatorio[0]))
elif aleatorio[0] == 'pedra' and escolha == 'papel':
    print('GANHOU\nSUA ESCOLHA: {}\nESCOLHA DO COMPUTADOR: {}\n'.format(escolha, aleatorio[0]))
else:
    print('PERDEU\nSUA ESCOLHA:{}\nESCOLHA DO COMPUTADOR: {}\n'.format(escolha, aleatorio[0]))


