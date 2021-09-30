#Desafio73
#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol
#na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados
#B) Os últimos 4 colocados da tabela
#C) Uma lista com os times em ordem alfabética
#D) Em qual posição na tabela está o time da Chapecoense

times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino',
         'Corinthias', 'Internacional', 'Fluminense', 'Athletico-PR', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'São Paulo', 'Juventos', 'América-MG',
         'Santos', 'Bahia', 'Grémio', 'Sport Recife', 'Chapecoense')

print("**"*30)
print(f"Lista de times do Brasileirão: {times}")
print("**"*30)
print(f"Os 5 primeiros são: {times[0:5]}")
print("**"*30)
print(f"Os 4 últimos são: {times[16:]}")
print("**"*30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("**"*30)
print(f"O Chapecoense está na {times.index('Chapecoense')} posição")

