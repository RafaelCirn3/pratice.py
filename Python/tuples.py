
#a tupla é uma lista imutável, não é possivel ordenar, adicionar ou remover elementos de uma lista
tupla = ('item1', 'item2', 'item3')
print(tupla)
print(len(tupla))
print(type(tupla))

lista = list(tupla) # transforma a tupla em uma lista, podendo alterar dados
print(lista)

tupla = tuple(lista) # transforma a lista em uma tupla, bloqueando a alteração de dados
print(tupla)

(x,y,z) = tupla
print('x',x)
print('y',y)
print('z',z)