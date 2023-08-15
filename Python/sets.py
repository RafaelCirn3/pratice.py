#sets são coleções não ordenadas, imutaveis que não permite valores duplicados, sendo conhecidos como conjuntos



numbers = {"1","2","3","4","5","6","7","8","9","10"}
print(type(numbers))


for x in numbers:
    print(x)
print("10" in numbers) #verifica se o elemnto está presente no set

numbers.add("11")
print(numbers)

text = {"um", "dois", "três", "quatro", "cinco"} #
numbers.update(text)
print(numbers)



# a diferença entre dicts e sets, é que dicts são ordenados e categorizados por suas chavesm já os sets
#são aleatórios     



#set.pop() remove o ultimo item de um set, mas por ser aleatório poderá remover qualquer um
#set.remove("nome do item") remove um item especifico
#set.discard discarta um item especifico no set
#set.clear limpa os elemnentos presentes no set
'''comparação de dicts e sets'''
dicts = {"1": "4"}
sets = {"1", "2"}

print(dicts.items())
print(dicts.keys())
print(sets)
print(sets.union(dicts))
print(sets.difference(dicts))

#union unifica elementos presentes  em sets ( podendo utilizar .update para apenas atualizar o primeiro conjunto )
#intersection apresente as igualdades entre sets
#summetric_difference apresenta somente a diferença entre sets