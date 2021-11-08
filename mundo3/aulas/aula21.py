#Interactive Help
# help(print)
print(input.__doc__)

def contador(i, f ,p):
    """
    -> Faz uma contagem e mostrar na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo
    :return: sem retorno
    """


def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')
    

somar(3, 2, 5)
somar(8, 4)