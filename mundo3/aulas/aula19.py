#Dicionário

pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 22}

del pessoas['sexo']
pessoas['nome'] = 'Lucassss'
pessoas['peso'] = 98.5

print(pessoas)
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")

print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')


