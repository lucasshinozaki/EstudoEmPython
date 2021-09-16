from datetime import date

ano = int(input('Digite o ano: '))
ano_atual = date.today()

if(ano_atual.year - ano) <= 9:
    print('MIRIM, IDADE:{}'.format(ano_atual.year - ano))
elif(ano_atual.year - ano) <= 14:
    print('INFANTL, IDADE:{}'.format(ano_atual.year - ano))
elif(ano_atual.year - ano) <= 19:
    print('JUNIOR, IDADE:{}'.format(ano_atual.year - ano))
elif(ano_atual.year - ano) <= 20:
    print('SÊNIOR, IDADE:{}'.format(ano_atual.year - ano))
else:
    print('MASTER, IDADE:{}'.format(ano_atual.year - ano))
