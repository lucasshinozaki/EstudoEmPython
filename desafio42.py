a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))

if a < b + c and b < a + c and c < a + b:
    print('é um triangulo')
    if a == b == c:
        print('equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isoceles')

else:
    print('Não é um triangulo')