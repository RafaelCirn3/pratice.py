cidades = []
valores = []

def MostrarValor(bebida, bebida2):
    resposta = input('Qual bebida você quer saber o valor mais econômico? ')
    
    if resposta.lower == 'pitu':
        print('O valor da Pitu é:', bebida)
    elif resposta == '51':
        print('O valor da 51 é:', bebida2)
    else:
        print('Opção inválida')

for cidade in range(3):

    cidade = input('digite o nome da cidade: ')
    cidades.append(cidade)

    for valor in range(1):
        linha = []    
        bebida= float(input('digite o valor da pitu:'))
        bebida2 = float(input('digite o valor da 51: '))
        linha.append(bebida)
        linha.append(bebida2)
        
    valores.append(linha)

print(cidades)
print(valores)

for cidade, linha in zip(cidades,valores):
        print('na cidade',cidade,'o valor das bebidas é:',linha)        



MostrarValor(bebida,bebida2)
