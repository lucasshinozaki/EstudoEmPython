from datetime import date

ano = int(input('Ano de nascimento: '))

ano_atual = date.today()

if (ano_atual.year - ano) == 18:
    print('Voce tem que se alistar esse ano')
elif (ano_atual.year - ano) < 18:
    print('Voce ainda vai se alistar: falta {} anos'.format(18 - (ano_atual.year - ano)))
else:
    print('Voce ja tinha que ter se alistador: {} anos se passaram'.format((ano_atual.year - ano) - 18))


