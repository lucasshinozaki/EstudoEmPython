n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if 5 <= media <= 6.9:
    print('RECUPERAÇÃO: NOTA:{:.2f}'.format(media))
elif media < 5:
    print('REPROVADO: NOTA:{:.2f}'.format(media))
else:
    print('APROVADO: NOTA:{:.2f}'.format(media))
    