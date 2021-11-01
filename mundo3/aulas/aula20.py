def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num}')
    # for valor in num:
    #     print(valor,end="")


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 4)
soma(5, 4, 5)
contador(2, 1, 5)
contador(8, 0)
contador(1, 2, 3, 4, 3)