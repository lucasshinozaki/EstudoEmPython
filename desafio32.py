ano = int(input('Digite o ano: '))

# Se o ano não for terminado em 00, e for divisivel por 4 ele eh bissexto
# Se o ano for terminado em 00, e for divisivel por 400 ele eh bissexto
# se ele não atender as essas condições, ele não bissexto

if ano % 100 == 0:
    if ano % 400 == 0:
        print('Ele é Bissexto')
    else:
        print('Não eh Bissexto')
else:
    if ano % 4 == 0:
        print('Ele é Bissexto')
    else:
        print('Não eh Bissexto')





