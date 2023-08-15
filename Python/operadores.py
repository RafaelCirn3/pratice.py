# operadores de comparação
"""
== igualdade
!= diferença
> maior que
< menor que
<= menor igual á
>= maior igual á """


"""operadores de associação

operador in -x in y
operador in -x not in y"""

x = "Rafael"
y = "Rafa"

print(y in x)
print("Dan" in x)


"""como achar o fatorial de um numero  4!"""
fatorial = 0 
numero = int(input("insira um numero"))
if numero < 0 :
    print('fatorial inexistente')
elif numero == 0: 
    print(f'fatorial de 0 é 1')
else:
    for x in range(1, numero+1)
    fatorial = fatorial*x
    print(f"o fatorial de{numero} é : {numero}")


"""numeros primos"""
numero = int(input('digite um numero e saiba se é primo'))
if numero > 1:
    for x in range(2,numero)
        if(numero % x) == 0 :
            print('nao é primo')
            break
        else:
            print('numero primo')
else:
    print('numero - ou = à 1 não pode ser primo')

