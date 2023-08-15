lista = ['chicago', 'queens', 'salvador', 'pernambuco', 10.6, 9, True]
print(lista) # apresenta a lista
print(type(lista))# apresenta o tipo da variável 
print(lista[4]) # apresenta o objeto 4
print(lista[1:4])# apresenta do objeto 1 ao objeto 4
print(lista[::]) # apresenta tudo
print(lista[0:6:2])# apresenta de 2 em 2 
print(len(lista)) #len apresenta o numero de objetos dentro da lista(o tamanho da lista basicamente)

#funções de dados numéricos: ex: somatório(sum); maior elemento da lista(max); menor elemento da lista(min)


#função list:
valor = range(11)

lista_numerica = list(range(11))
print(lista_numerica)


#alterando itens

animais = ["gato", "cachorro", "pombo", "peixe"]
print(animais)
animais[2] = "canario"
print(animais)
animais[2:4] = "leão", "tubarão"
print(animais)
print(len(animais))

#For para listas

for x in lista: #lista cada item dentro da lista 
    print(lista)

for x in range(len(lista)): # apresenta a variavel e identifica a posição dela
    print(x, lista[x])

#listagem de cada caractere inserido
texto = 'carro, avião'
lista2 = list(texto)
print(lista2)

#corrigindo apresentação dos caracteres inseridos
texto = texto.split(", ")
print(texto)


#adicionar itens

lista.append("moto")#adiona-se um item ao fim da lista
print(lista)

for x in range(len(lista)):
    print(x, lista[x])


lista.insert(0,"bicileta")#adiciona-se um item a lista, definindo a posição dele
print(lista)

for x in range(len(lista)):
    print(x, lista[x])


lista.extend(["caminhão", "triciclo"])#cria-se uma lista, que será desconstruída e adicionará a  quantidade de itens dentro dessa lista para a outra
print(lista)

for x in range(len(lista)):
    print(x, lista[x])

#removendo elementos da lista
lista.pop()#remove o ultimo item da lista, ou um item especifico a partir do index dele: lista.pop(0) remove o item 0
lista.remove()#remove um item específico dentro da lista
del lista#apaga a lista
lista.clear()#apaga todos os itens de uma lista exemplo: limpar carrinho de compras
lista.sort()#imprime os elementos em ordem alfabética; lista.sort(reverse) imprime em ordem decrescente 

#copiando itens de lista
lista2 = ['banana', '696969']#dessa forma copiamos cada item dentro de lista2 e incluimos em lista
for x in lista2
    lista.append(x)
print(lista)