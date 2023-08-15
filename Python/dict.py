#dicionários são uma coleção não ordenada, mutável que não permite valores duplicados

dict = {"nome": "Rafa:", "idade:": "17", "região:": "PB"}
print(dict["nome"])
print(dict.get("idade"))
print(dict.keys())
print(dict.values())
print(dict.items())

dict["região"] = "DF"
print(dict["região"])

dict.update({"região": "PB"})
print(dict["região"])

dict.update({"S/N": True})
print(dict)
'''
dict.popitem() # elimina o ultimo elemento dicionario
print(dict)


dict.pop("região") # elimina um elemento pela chave
print(dict)'''

for x in dict: #imprime cada elemento
    print(x, dict[x])

for x, y in dict.items():
    print(x,y)

print(dict.items())
print(dict.values())

chaves = ('item1', 'item2', 'item3')
valores = (0,1,2)
dict = dict.fromkeys(chaves, valores) #fromkeys define um valor de tuplas em chaves para um dicionario
print(dict)

pai = {"nome":"Daniel","idade":"26",
    "filho": {"nome": "Eduardo","idade":"3"}}

print(pai)