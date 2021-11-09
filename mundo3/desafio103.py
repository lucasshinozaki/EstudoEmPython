#Desafio 103
#Daça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos
#gols ele marcou
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(n='', g=''):
    if n == '' and g == '':
        print('O jogador <desconhecido> fez 0 gol(s) no campeonato;')
    elif n == '':
        print(f'O jogador <desconhecido> fez {g} gol(s) no campeonato;')
    elif g == '':
        print(f'O jogador {n} fez 0 gol(s) no campeonato;')
    else:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de Gols: '))
ficha(nome, gols)
