def perimetro(x,y):
    return (x*2) + (y*2)
h = int(input('digite um número: '))
l = int(input('digite um número: '))
r = perimetro(h,l)
print (r)



def nota(x,y,z):
    return (x+y+z) / 3
nota1 = int(input('digite um número: '))
nota2 = int(input('digite um número: '))
nota3 = int(input('digite um número: '))
nf = nota(nota1,nota2,nota3)
if nf>= 7:
    print('aprovado')
else:
    print('reprovado')




def viagem(x,y):
    vm =  x/y
    return vm
kmstart = float(input("Digite a quilometragem inicial: "))
kmf = float(input("Digite a quilometragem final: "))
horastart = float(input("Digite a hora inicial: "))
horaf= float(input("Digite a hora final: "))
distancia_percorrida = kmf - kmstart
tempo_percorrido = horaf - horastart
velocidade_media = viagem(distancia_percorrida, tempo_percorrido)
print("A velocidade média do veículo foi de", velocidade_media, "km/h.")



def mercado(preco, quantidade):
    vt = preco * quantidade
    return vt
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade adquirida: "))
total = mercado(preco, quantidade)
print("O valor total a ser pago é R$", total)



def checkpos(numero):
    if numero >= 0:
        return "O número é positivo."
    else:
        return "O número é negativo."
def lerNumeroInteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")
numero = lerNumeroInteiro()
resultado = checkpos(numero)
print(resultado)


def encontrar_maior(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
maior_numero = encontrar_maior(numero1, numero2)
print("O maior número digitado é:", maior_numero)


import math 
def calcular_volume(raio):
    volume = (4/3) * math.pi * (raio**3)
    return volume
raio = float(input("Digite o raio da esfera: "))
volume_esfera = calcular_volume(raio)
print("O volume da esfera é:", volume_esfera)



def calculadora(x, y, operacao):
    if operacao == '+':
        resultado = x + y
    elif operacao == '-':
        resultado = x - y
    elif operacao == '*':
        resultado = x * y
    elif operacao == '/':
        resultado = x / y
    else:
        print("Operação inválida.")
        return None
    return resultado
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
operacao = input("Digite o símbolo da operação (+, -, *, /): ")
resultado = calculadora(x, y, operacao)
if resultado is not None:
    print("Resultado:", resultado)


def conversor(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))
resultado = conversor(horas, minutos, segundos)
print("O total de segundos é:", resultado)



def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media
def calcular_diferenca(num1, num2):
    if num1 > num2:
        diferenca = num1 - num2
    else:
        diferenca = num2 - num1
    return diferenca
def calcular_produto(num1, num2):
    produto = num1 * num2
    return produto
def calcular_divisao(num1, num2):
    if num2 != 0:
        divisao = num1 / num2
        return divisao
    else:
        return "Erro: Divisão por zero!"
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
print("Escolha a operação:")
print("1 - Média entre os números digitados")
print("2 - Diferença do maior pelo menor")
print("3 - Produto entre os números digitados")
print("4 - Divisão do primeiro pelo segundo")
opcao = int(input("Digite o número da operação desejada: "))
if opcao == 1:
    resultado = calcular_media(x, y)
elif opcao == 2:
    resultado = calcular_diferenca(x, y)
elif opcao == 3:
    resultado = calcular_produto(x, y)
elif opcao == 4:
    resultado = calcular_divisao(x, y)
else:
    resultado = "Opção inválida!"

print("Resultado:", resultado)