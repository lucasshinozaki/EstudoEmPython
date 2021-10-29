# Desafio 95
# Aprimorar o DESAFIO 93 para que ele juncione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

list_jogadores = list()
jogador = dict()
lista_gols = list()

opcao = soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c}? '))
        soma += gols
        lista_gols.append(gols)
    jogador['gols'] = lista_gols[:]
    lista_gols.clear()
    jogador['total'] = soma
    list_jogadores.append(jogador.copy())
    soma = 0
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    print("-" * 20)
    if opcao == 'N':
        break

print("=-" * 30)
print(list_jogadores)
print("=-" * 30)
print(f'cod.     nome       gols        total')
print("--" * 30)
for i, j in enumerate(list_jogadores):
    print(f"{i}", end="    ")
    for k, v in j.items():
        print(f"{v}", end="         ")
    print()
print("--" * 30)

opcao = 0
while True:
    cont = 0
    opcao = int(input("Mostrar dados de qual jogador? "))

    for i, j in enumerate(list_jogadores):
        if i == opcao:
            print(f"--LEVANTAMENTO DO JOGADOR {j['nome']}")
            for k in j['gols']:
                print(f'    => Na partida {cont}, fez {k} gols.')
                cont += 1
    if opcao == 999:
        break
    elif opcao > len(list_jogadores) - 1 or opcao < 0:
        print(f"ERRO! Não existe jogado com código {opcao}: Tente novamento")
print("<< VOLTE SEMPRE >>")