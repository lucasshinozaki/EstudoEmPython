#Lista parte 1

num = [1, 5, 9, 1]
num[2] = 3

#Adicionando dados
num.append(7)
#deixando em ordem
num.sort()
#deixando em ordem reversa
num.sort(reverse=True)
#inserido um daodo na posição 2
num.insert(2, 0)
#retirando o dado da posição 2
num.pop(2)
#remoce o elemento 2, somente o primeiro
num.remove(2)
#Verificação se tem 4 na lista e remove
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numero 4")
print(num)
print(f"Essa lista tem {len(num)} elementos")
