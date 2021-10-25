#Desafio 92
#Crie um programa que leia nome, ano de nascimento e carteiro de trabalho e cadastre-os (com idade) em um dicionário
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o sálario
#Calculer e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

dados = dict()

dados['nome'] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
dados['idade'] = 2021 - nascimento
dados['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$ "))
    dados['aposentadoria'] = (dados['contratacao'] - nascimento) + 35

print("=-"*30)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')