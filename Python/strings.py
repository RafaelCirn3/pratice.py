# a string pode ser escrita com aspas duplas ou simpoes " '' "
print('hello')
# a string  em aspas triplas cria um texto em bloco

print("""texto criado
com quebra de linha
aplicada ao codigo""")
# .strip() faz com que a area anterior e posterior ao código sejam ignorados
b = " exemplo 1"
print(b)
print(b.strip())
# .lower() deixa todo o texto minusculo
c = "exemplo"
print(c)
print(c.lower())
# .upper deixa todo o texto maiusculo
d = 'exemplo'
print(d)
print(d.upper())

# print(type(variavel)) nos mostra o tipo da variavel selecionada
# casting é a conversão de tipo de variável, como exemplo transformar o valor
# float 3.1 em int, sendo assim o valor apresentado será "3"
float1 = float(3.2)
float2 = float("2")
float3 = float(5)

print(float1, float2, float3)
print(type(float2))

M = 5
print(M, " variavel global")


def funcao():
    M = 10
    print(M, 'variavel local')


funcao()

nome = "Rafael"
altura = 1.85
cpf = "000.000.000-00"
idade = 17
