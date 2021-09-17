#Desafio 62
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

cont = 1
while cont != 10:
    print('{} : {}'.format(cont, primeiro_termo))
    primeiro_termo += razao
    cont += 1

quantidade = 1
print('''Digite uma opcao:
   [1] - Continuar
   [2] - Sair
   ''')
opcao = int(input('Escolha uma das opções: '))
if opcao == 1:
    while quantidade != 0:
        print('Digite 0 na quantidade de se quiser para o programa')
        quantidade = int(input('Digite a quantidade de termos: '))
        for c in range(cont, quantidade + cont):
            print('{} : {}'.format(cont, primeiro_termo))
            primeiro_termo += razao
            cont += 1
else:
    print("Saindo do programa agora...")