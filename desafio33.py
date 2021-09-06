n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 > n2:
    if n1 > n3:
        print('O maior eh: {}'.format(n1))
        if n2 < n3:
            print('O menor eh: {}'.format(n2))
        else:
            print('O menor eh: {}'.format(n3))
    else:
        print('O maior eh: {}'.format(n3))
else:
    if n2 > n3:
        print('O maior eh: {}'.format(n2))
    else:
        print('O maior eh: {}'.format(n3))
    if n1 < n3:
        print('O menor eh: {}'.format(n1))
    else:
        print('O menor eh: {}'.format(n3))
