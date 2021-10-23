#Desafio 90
#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
#No final mostre o conteúdo da estrutura na tela

ficha = dict()
ficha['nome'] = str(input("Nome: "))
ficha['media'] = float(input(f"Média de {ficha['nome']}: "))

if ficha['media'] > 7:
    ficha['situacao'] = 'APROVADA'
else:
    ficha['situacao'] = 'REPROVADA'

for k, v in ficha.items():
    print(f'{k} é igual a {v}')
