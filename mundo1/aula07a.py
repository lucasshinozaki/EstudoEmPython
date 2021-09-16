n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \no produto é {} e \na divisão é {:.3}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
