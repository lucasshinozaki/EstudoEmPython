#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro número: '))
opcao = 6

while opcao != 5:
    print('''Menu:
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do Programa
    ''')
    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {:.2f} + {:.2f} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {:.2f} * {:.2f} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior é: {}'.format(n1))
        else:
            print('O maior é: {}'.format(n2))
    elif opcao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print("Opção inválida. Tente novamente")
    print("=-=" * 10)
print("Fim do programa! Volte Sempre!!")

