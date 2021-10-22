#Desafio 89
#Cire um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
#De cada auluno individualmente

listaComposta = list()
nomes = list()
notas = list()
mediaList = list()

while True:
    listaComposta.append(str(input("Nome: ")))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    media = (notas[0] + notas[1]) / 2
    mediaList.append(media)
    notas.append(mediaList[:])
    listaComposta.append(notas[:])
    mediaList.clear()
    notas.clear()
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    if opcao == 'N':
        break
print("-="*30)

print(listaComposta)

cont = cont2 = 0
print("No.")
for boletim in listaComposta:
    if cont % 2 == 0:
        print(f"{cont2:<5}", end=" ")
        print(f"{boletim:<8}", end=" ")
        cont2 += 1
    else:
        print(f"{boletim[2][0]:<10}")
    cont += 1


while True:
    cod = int(input("Mostrar notas de qual aluno? (999 interrompe:) "))
    if cod % 2 == 0:
        print(f"Notas de {listaComposta[cod]} são {listaComposta[cod + 1][0]} e {listaComposta[cod + 1][1]}")
    else:
        cod += 1
        if cod == 1:
            print(f"Notas de {listaComposta[cod]} são {listaComposta[cod + 1][0]} e {listaComposta[cod + 1][1]}")
        else:
            print(f"Notas de {listaComposta[cod]} são {listaComposta[cod + 1][0]} e {listaComposta[cod + 2][1]}")
    if cod == 999:
        break