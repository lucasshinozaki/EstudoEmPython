#Desafio 54:
#Crie um program que leia o ano de nascimento de sete pessoas
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#E quantas já são maiores

from datetime import date

ano_atual = date.today().year
cont1 = 0
cont2 = 0

for c in range(0, 7):
    ano = int(input("Digite o ano de nascimento: "))
    if (ano_atual - ano) >= 18:
        cont1 += 1
    else:
        cont2 += 1

print("Quantidade de maiores de idade: {}".format(cont1))
print("Quantidade de menores de idade: {}".format(cont2))
