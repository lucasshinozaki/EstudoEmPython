#Desafio 101
#Crie um programa que tenha uma função chamada voto() que vai recever como parâmetro o ano de nascimento de uma pessoa
#Retornando um valor literal indicando se uma pessoa tem voto
#NEGADO, OPCIONAL ou OBRIGATORIO na eleoções
from datetime import date

def voto(idade):
    if idade < 16:
        return 'NEGADO'
    elif idade >= 16 and idade < 18:
        return 'OPCIONAL'
    elif idade >= 18 and idade < 65:
        return 'OBRIGATORIO'
    else:
        return 'OPCIONAL'


nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
print(f'Com {idade} anos: VOTO {voto(idade)}.')
