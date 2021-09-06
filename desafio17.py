import math
num1 = float(input('Digite um cateto :'))
num2 = float(input('Digite outro cateto :'))

hip = math.hypot(num1, num2)

hip1 = (((num1 * num1) + (num2 * num2)) ** (1/2))


print('O valor da hipotenusa eh {:.2f}'.format(hip1))
