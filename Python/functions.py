#Paradigma Imperativo, faz com que ele obedeça linha por linha do seu código
# def cria uma função específica 
nome = "Rafael" #variável Global

#SEMPRE COLOCAR UM ESPAÇO DE 2 LINHAS ENTRE FUNCTIONS E SEU CÓDIGO
def meu_nome():
    nome = "Bjorn" # variável local
    print(nome)
#SEMPRE COLOCAR UM ESPAÇO DE 2 LINHAS ENTRE FUNCTIONS E SEU CÓDIGO
#SEMPRE COLOCAR UM ESPAÇO DE 2 LINHAS ENTRE FUNCTIONS E SEU CÓDIGO
def contar_10():
    for x in range(10):
        print(x+1) 
#SEMPRE COLOCAR UM ESPAÇO DE 2 LINHAS ENTRE FUNCTIONS E SEU CÓDIGO

print(nome) # apresentando a variável global
meu_nome() # definindo o que acontecerá no código, seguindo o que está presente na function
contar_10()

#Utilização do Returno


lista = [1,2,3,4,5]
print(lista)
retornar = lista.pop()
print(lista)
print('a função pop retorna: ', retornar)
hello = print('olá mundo')
print("a função retornou :", hello)


def ola_mundo():
    return ('ola mundo') #utilizando o return ao invés do print, faz com que precisamos definir o que irá retornar, deixando ela mais reutilizável


retorno = ola_mundo()
print(retorno)


def par_impar():
            num = int(input('digite um número inteiro: '))
            if (num % 2) == 0 :
                return "numero par"
            return "numero impar"




def saindo():
    x = 0
    if x == 1:
        return 'saindo da função 1'
    return 'saindo da função 2'

print (saindo())