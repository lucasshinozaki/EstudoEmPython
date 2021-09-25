# Desafio 69
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final mostre:
#   A - Quantas pessoas tem mais de 18 anos
#   B - Quantos homens foram cadastrados
#   C - Quantas mulheres tem menos de 20 anos

opcao = sexo = cont1 = cont2 = cont3 = 0
while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F]: ").strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = input("Sexo: [M/F]: ").strip().upper()[0]
    print("-" * 30)
    opcao = input("Quer continuar? [S/N]: ").strip().upper()[0]
    print("-" * 30)
    while opcao not in 'SsNn':
        opcao = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if sexo == 'F' and idade < 20:
        cont3 += 1
    if idade > 18:
        cont1 += 1
    if sexo == 'M':
        cont2 += 1
    if opcao == 'N':
        break


print(f"Total de pessoa com mais de 18 anos: {cont1}")
print(f"Ao todo temos {cont2} homens cadastrados")
print(f"E temos {cont3} mulheres com menos de 20 anos")