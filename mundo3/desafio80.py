#Desafio 80
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista
#Já na posição correta de inserção(sem usar o sort()).
#No final, mostre a lista ordenada na tela

valores = []

for c in range(0, 5):
    valor = int(input("Digite um valor: "))
    if c == 0:
        print("Adicionando no final da lista")
        valores.append(valor)
    else:
        if min(valores) > valor:
            print("Adicionado na posição 0 da lista...")
            valores.insert(0, valor)
        elif max(valores) < valor:
            print("Adicionando no final da lista")
            valores.append(valor)
        elif valor < valores[1]:
            print("Adicionado na posição 1 da lista...")
            valores.insert(1, valor)
        elif valor < valores[2]:
            print("Adicionado na posição 2 da lista...")
            valores.insert(2, valor)
        elif valor < valores[3]:
            print("Adicionado na posição 3 da lista...")
            valores.insert(3, valor)

print(f"Os valores digitados em ordem foram: {valores}")