#  """inpuit é a função ao qual você pede para o cliente definir uma variável """

 nome = input("qual seu nome ?")
 print("prazer em te conhecer", nome)

 nome = input("meu nome é: ")
 idade = int(input("minha idade é: "))
 print("meu nome é {0} e minha idade é {1}".format(nome, idade))

numero = int(input('digite um numero:'))

if numero > 0:
    print('numero positivo')
elif numero == 0:
    print('numero = 0')
elif numero  != [1, 2, 3,4,5,6,7,8,9,0]:
    print(' nao é um numero')
else:
    print('numero negativo')


#  o laço continue ignora certo objeto exemplo num == 3 : continue; ele ignora o numero 3
#   o pass ignora a identação vazia


nome = 'chicago'
for x in nome:
    print(x, end=' ° ')
