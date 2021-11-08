#Desafio 102
#Crie um programa que tenha um função fatoria() que receba dois parâmetros
#o primeiro que indique o número a calcular e o outro chamaddo show que será um valor lógico (opcional)
#Indicando se será mostrado ou não na tela o processo de cálculo do Fatorial

def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um numero
    :param num: O numero a ser calculado
    :param show: [opcional] Mostra ou não a conta
    :return: O valor do fatorial de um numero n
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print("1 =", end=" ")
                return f
            print(f'{c} x', end=" ")
    return f


print(fatorial(5, True))
print(fatorial(2, True))
help(fatorial)
