teste = list()
teste.append("Lucas")
teste.append(22)
print(teste)

galera = list()
galera.append(teste[:]) #Fazendo uma copia do teste[:]

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[0][0])

for pessoa in galera:
    print(f'Nome: {pessoa[0]} tem Idade: {pessoa[1]}')

galera3 = list()
dado = list()

totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmenor += 1

print(f"Temos {totmaior} maiores e {totmenor} menores de idade")