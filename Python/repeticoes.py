# estrutura de repetições
# while
# for
# do while (não existe em python, mas é possível fazer, o do while executa e
# depois verifica o código)

a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f'a não é menor ou igual à 5 . valor de {a}.')


s = 'pernambuco'

for x in s:
    print(x)


for x in range(6):
    # em range, o número representa
    # quanto digítos serão feitos, ou seja de 0-5
    print(x)


for x in range(5, 8):
    print(x)

#              x   z   y
for x in range(5, 30, 5):
    print(x)


for x in range(6):
    print(x)
else:
    print('chegamos no fim ')


#do while, utiliza boolean

palpite =  10
numero = 9 

#while bool(palpite) is True (ele verifica e depois imprime)
while True: 
    print('adivinhe o numero')
    palpite = int(input())
    if palpite == numero:
        print('acertou')
        break
    else:
        print('errou')
else:
    print('erro na aplicação')
    print(bool(palpite))
